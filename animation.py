import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec


def create_projectile_animation(trajectory: dict):
    """
    Create an animation showing projectile position,
    vertical velocity and vertical acceleration.
    """

    time = trajectory["time"]
    x_position = trajectory["x_position"]
    y_position = trajectory["y_position"]
    y_velocity = trajectory["y_velocity"]
    y_acceleration = trajectory["y_acceleration"]

    figure = plt.figure(figsize=(10, 5))

    grid = GridSpec(
        2,
        2,
        figure=figure,
        width_ratios=[2, 1],
    )

    trajectory_axis = figure.add_subplot(grid[:, 0])

    trajectory_axis.set_xlim(
        0,
        max(float(np.max(x_position)) * 1.05, 1),
    )

    trajectory_axis.set_ylim(
        0,
        max(float(np.max(y_position)) * 1.20, 1),
    )

    trajectory_line, = trajectory_axis.plot(
        [],
        [],
        linewidth=2,
        color="#4285F4",
    )

    ball, = trajectory_axis.plot(
        [],
        [],
        "ro",
        markersize=7,
    )

    trajectory_axis.set_xlabel("Horizontal Distance (m)")
    trajectory_axis.set_ylabel("Height (m)")
    trajectory_axis.set_title("Projectile Trajectory")
    trajectory_axis.grid(True, alpha=0.3)

    velocity_axis = figure.add_subplot(grid[0, 1])

    velocity_limit = max(
        float(np.max(np.abs(y_velocity))) * 1.20,
        1,
    )

    velocity_axis.set_xlim(0, float(time[-1]))
    velocity_axis.set_ylim(-velocity_limit, velocity_limit)

    velocity_line, = velocity_axis.plot(
        [],
        [],
        linewidth=2,
        color="#EA4335",
    )

    velocity_axis.axhline(
        y=0,
        color="black",
        linestyle="--",
        alpha=0.4,
    )

    velocity_axis.set_xlabel("Time (s)")
    velocity_axis.set_ylabel("Vertical Velocity (m/s)")
    velocity_axis.grid(True, alpha=0.3)

    acceleration_axis = figure.add_subplot(grid[1, 1])

    gravity = abs(float(y_acceleration[0]))

    acceleration_axis.set_xlim(0, float(time[-1]))
    acceleration_axis.set_ylim(-2 * gravity, gravity)

    acceleration_line, = acceleration_axis.plot(
        [],
        [],
        linewidth=2,
        color="#34A853",
    )

    acceleration_axis.set_xlabel("Time (s)")
    acceleration_axis.set_ylabel("Acceleration (m/s²)")
    acceleration_axis.grid(True, alpha=0.3)

    frame_count = min(40, len(time))

    frame_indices = np.linspace(
        1,
        len(time),
        frame_count,
        dtype=int,
    )

    frame_indices = np.unique(frame_indices)

    def update(frame):
        time_data = time[:frame]
        x_data = x_position[:frame]
        y_data = y_position[:frame]
        velocity_data = y_velocity[:frame]
        acceleration_data = y_acceleration[:frame]

        trajectory_line.set_data(x_data, y_data)

        if len(y_data) > 0:
            ball.set_data(
                [x_data[-1]],
                [y_data[-1]],
            )

            velocity_line.set_data(
                time_data,
                velocity_data,
            )

            acceleration_line.set_data(
                time_data,
                acceleration_data,
            )

        return (
            trajectory_line,
            ball,
            velocity_line,
            acceleration_line,
        )

    animation = FuncAnimation(
        figure,
        update,
        frames=frame_indices,
        interval=40,
        blit=True,
        repeat=False,
    )

    figure.tight_layout()

    return figure, animation