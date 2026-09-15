import numpy as np


GRAVITY_VALUES = {
    "Earth": 9.81,
    "Moon": 1.62,
    "Mars": 3.71,
}


def calculate_trajectory(
    initial_velocity: float,
    angle_degrees: float,
    gravity: float = 9.81,
    time_step: float = 0.02,
) -> dict:
    "Calculate projectile position, velocity and acceleration."

    if initial_velocity <= 0:
        raise ValueError("Initial velocity must be greater than zero.")

    if not 0 < angle_degrees < 90:
        raise ValueError("Angle must be between 0 and 90 degrees.")

    if gravity <= 0:
        raise ValueError("Gravity must be greater than zero.")

    if time_step <= 0:
        raise ValueError("Time step must be greater than zero.")

    angle_radians = np.radians(angle_degrees)

    flight_time = (
        2 * initial_velocity * np.sin(angle_radians) / gravity
    )

    number_of_points = max(
        2,
        int(np.ceil(flight_time / time_step)) + 1,
    )

    time = np.linspace(0, flight_time, number_of_points)

    horizontal_velocity = initial_velocity * np.cos(angle_radians)
    initial_vertical_velocity = initial_velocity * np.sin(angle_radians)

    x_position = horizontal_velocity * time
    y_position = (
        initial_vertical_velocity * time
        - 0.5 * gravity * time**2
    )

    x_velocity = np.full_like(time, horizontal_velocity)
    y_velocity = initial_vertical_velocity - gravity * time

    x_acceleration = np.zeros_like(time)
    y_acceleration = np.full_like(time, -gravity)

    return {
        "time": time,
        "x_position": x_position,
        "y_position": y_position,
        "x_velocity": x_velocity,
        "y_velocity": y_velocity,
        "x_acceleration": x_acceleration,
        "y_acceleration": y_acceleration,
    }


def calculate_metrics(
    initial_velocity: float,
    angle_degrees: float,
    gravity: float = 9.81,
) -> dict:
    """Calculate the main measurements of projectile motion."""

    if initial_velocity <= 0:
        raise ValueError("Initial velocity must be greater than zero.")

    if not 0 < angle_degrees < 90:
        raise ValueError("Angle must be between 0 and 90 degrees.")

    if gravity <= 0:
        raise ValueError("Gravity must be greater than zero.")

    angle_radians = np.radians(angle_degrees)

    flight_time = (
        2 * initial_velocity * np.sin(angle_radians) / gravity
    )

    maximum_height = (
        initial_velocity**2
        * np.sin(angle_radians) ** 2
        / (2 * gravity)
    )

    horizontal_range = (
        initial_velocity**2
        * np.sin(2 * angle_radians)
        / gravity
    )

    return {
        "flight_time": flight_time,
        "maximum_height": maximum_height,
        "horizontal_range": horizontal_range,
    }
def calculate_state_at_time(
    initial_velocity: float,
    angle_degrees: float,
    selected_time: float,
    gravity: float = 9.81,
) -> dict:
    """Calculate projectile data at a selected time."""

    if initial_velocity <= 0:
        raise ValueError("Initial velocity must be greater than zero.")

    if not 0 < angle_degrees < 90:
        raise ValueError("Angle must be between 0 and 90 degrees.")

    if gravity <= 0:
        raise ValueError("Gravity must be greater than zero.")

    angle_radians = np.radians(angle_degrees)

    flight_time = (
        2 * initial_velocity * np.sin(angle_radians) / gravity
    )

    if not 0 <= selected_time <= flight_time:
        raise ValueError(
            "Selected time must be within the flight duration."
        )

    horizontal_velocity = (
        initial_velocity * np.cos(angle_radians)
    )

    vertical_velocity = (
        initial_velocity * np.sin(angle_radians)
        - gravity * selected_time
    )

    horizontal_position = (
        horizontal_velocity * selected_time
    )

    vertical_position = (
        initial_velocity
        * np.sin(angle_radians)
        * selected_time
        - 0.5 * gravity * selected_time**2
    )

    total_velocity = np.sqrt(
        horizontal_velocity**2
        + vertical_velocity**2
    )

    return {
        "time": float(selected_time),
        "horizontal_position": float(horizontal_position),
        "vertical_position": float(vertical_position),
        "horizontal_velocity": float(horizontal_velocity),
        "vertical_velocity": float(vertical_velocity),
        "total_velocity": float(total_velocity),
        "vertical_acceleration": float(-gravity),
    }