import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime  # Import datetime for time tracking

# Generate theta values in degrees for complex spirals with 113 rotations
theta_degrees = np.linspace(0, 113 * 360, 1000000)
theta_radians = np.deg2rad(theta_degrees)
z = np.exp(theta_radians * 1j) + np.exp(np.pi * theta_radians * 1j)
x = np.real(z)
y = np.imag(z)

# Set up the plotting area
fig, ax = plt.subplots(figsize=(13.5, 10.8))
ax.set_aspect('equal')
fig.patch.set_facecolor('#181818')
ax.set_facecolor('#181818')
ax.axis('off')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)

# variable speed if the number of frames is bigger
variable_speed_zoom_out = 200
variable_speed_medium_zoom = 200
variable_speed_close_zoom = 200 

# Speed settings for each phase (points per frame)
speeds = {
    'zoom_out': 10 * variable_speed_zoom_out,  # Adjust as needed for correct speed
    'medium_zoom': 10 * variable_speed_medium_zoom,  # Adjust as needed for correct speed
    'close_zoom': 10 * variable_speed_close_zoom,  # Adjust as needed for correct speed
}

# Duration of each zoom phase in seconds
phase_durations = {
    'zoom_out': 0,
    'medium_zoom': 00,
    'close_zoom': 10,
}

# Zoom scales for each phase
zoom_scales = {
    'zoom_out': 2.5,  # Fully zoomed-out scale
    'medium_zoom': 1.5,  # Medium zoom scale, adjust as needed
    'close_zoom': 0.4,  # Close zoom scale
}

# Record the start time of the animation
start_time = datetime.datetime.now()

def init():
    """Initialize the animation by clearing line and marker data."""
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    return ax,

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
    
    # Clear the axes to prevent any artifact buildup
    ax.clear()

    # Reapply the necessary settings to the axes
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.axis('off')
    
    # Calculate the number of points to display based on the current phase speed
    num_points = int(elapsed_time * speeds[current_phase]) % len(x)
    
    # Set plot limits and draw the line and marker
    if current_phase == 'zoom_out':
        # Set static plot limits for the zoomed-out phase
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.plot(x[:num_points], y[:num_points], color='#ccc', linewidth=1.2)
        # Increase the marker size to make it visible in the zoomed-out view
        ax.plot(x[num_points-1:num_points], y[num_points-1:num_points], 'o', color='white', markersize=2) # Adjusted size
    else:
        # Dynamically set plot limits to follow the marker
        zoom_scale = zoom_scales[current_phase]
        current_x = x[num_points-1] if num_points > 0 else 0
        current_y = y[num_points-1] if num_points > 0 else 0
        ax.set_xlim(current_x - zoom_scale, current_x + zoom_scale)
        ax.set_ylim(current_y - zoom_scale, current_y + zoom_scale)
        ax.plot(x[:num_points], y[:num_points], color='#ccc', linewidth=1.2)
        ax.plot(x[num_points-1:num_points], y[num_points-1:num_points], 'o', color='white', markersize=2) # Normal size

    return ax,


total_frames_for_video = 1000000  # This is an example value

# Set up and start the animation
ani = FuncAnimation(fig, update, init_func=init, frames=total_frames_for_video, interval=1, blit=False)

# Save the animation with high quality
#ani.save(r'E:\Windows Daily Usage\Documents\01 Berckan\Reveries\Youtube\programming\video\zoom_out.mp4', writer='ffmpeg', fps=60, bitrate=5000)
#ani.save(r'E:\Windows Daily Usage\Documents\01 Berckan\Reveries\Youtube\programming\video\zoom_middle.mp4', writer='ffmpeg', fps=60, bitrate=5000)
ani.save(r'E:\Windows Daily Usage\Documents\01 Berckan\Reveries\Youtube\programming\video\zoom_in.mp4', writer='ffmpeg', fps=60, bitrate=5000)

plt.show()

print("The video was successfully created and saved.")
#except Exception as e:
print(f"Failed to save the video")