import numpy as np
import pytest

from physics import calculate_metrics, calculate_trajectory


def test_projectile_starts_and_finishes_at_ground_level():
    trajectory = calculate_trajectory(
        initial_velocity=20,
        angle_degrees=45,
        gravity=9.81,
    )

    assert trajectory["y_position"][0] == pytest.approx(0)
    assert trajectory["y_position"][-1] == pytest.approx(
        0,
        abs=1e-10,
    )


def test_horizontal_velocity_remains_constant():
    trajectory = calculate_trajectory(
        initial_velocity=20,
        angle_degrees=45,
        gravity=9.81,
    )

    horizontal_velocity = trajectory["x_velocity"]

    assert np.allclose(
        horizontal_velocity,
        horizontal_velocity[0],
    )


def test_earth_metrics_for_known_launch():
    metrics = calculate_metrics(
        initial_velocity=20,
        angle_degrees=45,
        gravity=9.81,
    )

    assert metrics["flight_time"] == pytest.approx(
        2.883,
        rel=0.001,
    )

    assert metrics["maximum_height"] == pytest.approx(
        10.194,
        rel=0.001,
    )

    assert metrics["horizontal_range"] == pytest.approx(
        40.775,
        rel=0.001,
    )


def test_lower_gravity_produces_longer_range():
    earth_metrics = calculate_metrics(
        initial_velocity=20,
        angle_degrees=45,
        gravity=9.81,
    )

    moon_metrics = calculate_metrics(
        initial_velocity=20,
        angle_degrees=45,
        gravity=1.62,
    )

    assert (
        moon_metrics["horizontal_range"]
        > earth_metrics["horizontal_range"]
    )


@pytest.mark.parametrize(
    "velocity, angle, gravity",
    [
        (0, 45, 9.81),
        (-10, 45, 9.81),
        (20, 0, 9.81),
        (20, 90, 9.81),
        (20, 45, 0),
    ],
)
def test_invalid_inputs_raise_error(
    velocity,
    angle,
    gravity,
):
    with pytest.raises(ValueError):
        calculate_trajectory(
            initial_velocity=velocity,
            angle_degrees=angle,
            gravity=gravity,
        )