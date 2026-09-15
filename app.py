import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components

from animation import create_projectile_animation
from physics import (
    GRAVITY_VALUES,
    calculate_metrics,
    calculate_trajectory,
)


st.set_page_config(
    page_title="Projectile Motion Simulator",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Projectile Motion Simulator")

st.write(
    """
    Explore how launch velocity, launch angle and gravity affect
    the motion of a projectile.
    """
)

st.sidebar.header("Simulation Settings")

planet = st.sidebar.selectbox(
    "Select a celestial body",
    options=list(GRAVITY_VALUES.keys()),
)

gravity = GRAVITY_VALUES[planet]

initial_velocity = st.sidebar.slider(
    "Initial velocity (m/s)",
    min_value=1.0,
    max_value=100.0,
    value=20.0,
    step=1.0,
)

angle_degrees = st.sidebar.slider(
    "Launch angle (degrees)",
    min_value=1.0,
    max_value=89.0,
    value=45.0,
    step=1.0,
)

trajectory = calculate_trajectory(
    initial_velocity=initial_velocity,
    angle_degrees=angle_degrees,
    gravity=gravity,
)

metrics = calculate_metrics(
    initial_velocity=initial_velocity,
    angle_degrees=angle_degrees,
    gravity=gravity,
)

metric_column_1, metric_column_2, metric_column_3 = st.columns(3)

metric_column_1.metric(
    "Flight Time",
    f"{metrics['flight_time']:.2f} s",
)

metric_column_2.metric(
    "Maximum Height",
    f"{metrics['maximum_height']:.2f} m",
)

metric_column_3.metric(
    "Horizontal Range",
    f"{metrics['horizontal_range']:.2f} m",
)

st.subheader(f"Animated Trajectory on {planet}")

animation_figure, projectile_animation = (
    create_projectile_animation(trajectory)
)

animation_html = projectile_animation.to_jshtml()

components.html(
    animation_html,
    height=600,
    scrolling=False,
)

plt.close(animation_figure)
simulation_data = pd.DataFrame(
    {
        "Time (s)": trajectory["time"],
        "Horizontal Position (m)": trajectory["x_position"],
        "Vertical Position (m)": trajectory["y_position"],
        "Horizontal Velocity (m/s)": trajectory["x_velocity"],
        "Vertical Velocity (m/s)": trajectory["y_velocity"],
        "Vertical Acceleration (m/s²)": trajectory[
            "y_acceleration"
        ],
    }
)

st.subheader("Simulation Data")

st.dataframe(
    simulation_data,
    use_container_width=True,
)

csv_data = simulation_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Simulation Data as CSV",
    data=csv_data,
    file_name="projectile_simulation.csv",
    mime="text/csv",
)

st.caption(
    "Originally developed as a high-school physics visualisation "
    "project and redesigned as an interactive Python application."
)