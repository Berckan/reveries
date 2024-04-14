import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime  # Import datetime for time tracking

# Generate theta values in degrees for complex spirals with 113 rotations
theta_degrees = np.linspace(0, 113 * 360, 50000)
theta_radians = np.deg2rad(theta_degrees)
z = np.exp(theta_radians * 1j) + np.exp(np.pi * theta_radians * 1j)
x = np.real(z)
y = np.imag(z)

# Set up the plotting area
fig, ax = plt.subplots(figsize=(8, 12))
ax.set_aspect('equal')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
line, = ax.plot([], [], color='#ccc', linewidth=0.1)
marker, = ax.plot([], [], 'o', color='white', markersize=3)

# Speed settings for each phase (points per frame)
speeds = {
    'zoom_out': 105,  # High speed for zoomed-out view
    'medium_zoom': 50,  # Lower speed for medium zoom
    'close_zoom': 20,  # Lower speed for close zoom
}

# Duration of each zoom phase in seconds
phase_durations = {
    'zoom_out': 5,
    'medium_zoom': 5,
    'close_zoom': 5,
}

# Record the start time of the animation
start_time = datetime.datetime.now()

def init():
    """Initialize the animation by clearing line and marker data."""
    line.set_data([], [])
    marker.set_data([], [])
    return line, marker

def get_current_phase(elapsed_time):
    """Get the current phase based on elapsed time."""
    total_duration = sum(phase_durations.values())
    phase_time = elapsed_time % total_duration
    if phase_time < phase_durations['zoom_out']:
        return 'zoom_out'
    elif phase_time < phase_durations['zoom_out'] + phase_durations['medium_zoom']:
        return 'medium_zoom'
    else:
        return 'close_zoom'

def update(frame):
    """Update function to animate the spiral and adjust zoom levels dynamically."""
    elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
    current_phase = get_current_phase(elapsed_time)
    zoom_scale = 2.5 if current_phase == 'zoom_out' else (0.2 if current_phase == 'close_zoom' else 1.0)

    # Calculate the number of points to display based on the current phase speed
    num_points = int(elapsed_time * speeds[current_phase]) % len(x)
    line.set_data(x[:num_points], y[:num_points])
    marker.set_data(x[num_points-1:num_points], y[num_points-1:num_points])

    # Dynamically set plot limits to follow the marker
    if current_phase != 'zoom_out':
        current_x = x[num_points-1]
        current_y = y[num_points-1]
        ax.set_xlim(current_x - zoom_scale, current_x + zoom_scale)
        ax.set_ylim(current_y - zoom_scale, current_y + zoom_scale)
    else:
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)

    return line, marker

# Set up and start the animation
ani = FuncAnimation(fig, update, init_func=init, frames=np.arange(0, len(x)), interval=1, blit=True)

plt.show()
