import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Generating complex spirals
theta_degrees = np.linspace(0, 113 * 360, 50000)
theta_radians = np.deg2rad(theta_degrees)
z = np.exp(theta_radians * 1j) + np.exp(np.pi * theta_radians * 1j)
x = np.real(z)
y = np.imag(z)

# Create figure and axis with desired aesthetics
fig, ax = plt.subplots(figsize=(8, 12))
ax.set_aspect('equal')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
line, = ax.plot([], [], color='#ccc', linewidth=0.1)

def init():
    line.set_data([], [])
    return line,

# Animation interval and frame rate
interval = 5  # milliseconds per frame
fps = 1000 / interval  # frames per second
zoom_period = 10 * fps  # 10 seconds * frames per second

def update(frame):
    """Update function for the animation that processes every frame and dynamically zooms."""
    line.set_data(x[:frame], y[:frame])
    
    cycle_phase = (frame // zoom_period) % 2
    if cycle_phase == 0:  # Zoom out phase
        if frame < zoom_period:  # Only during the first cycle
            # Stay zoomed out and do not follow the line
            ax.set_xlim(-2.5, 2.5)
            ax.set_ylim(-2.5, 2.5)
    else:  # Zoom in phase
        # Follow the line with a tighter zoom
        if frame < len(x):
            current_x = x[frame]
            current_y = y[frame]
            zoom_scale = 0.9  # Defines the zoom level, smaller value = tighter zoom
            ax.set_xlim(current_x - zoom_scale, current_x + zoom_scale)
            ax.set_ylim(current_y - zoom_scale, current_y + zoom_scale)

    return line,

num_frames = len(x)

# Animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=interval)

# Display the animation
plt.show()

# Optional: save the animation
# ani.save(r'E:\Windows Daily Usage\Desktop\coso.mp4', writer='ffmpeg', fps=60, bitrate=5000, savefig_kwargs={'facecolor': 'black'})
