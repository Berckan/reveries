import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter

# Create an array of theta values in degrees
theta_degrees = np.linspace(0, 113 * 360, 10000)

# Convert degrees to radians
theta_radians = np.deg2rad(theta_degrees)

# Calculate z(theta) using the formula
z = np.exp(theta_radians * 1j) + np.exp(np.pi * theta_radians * 1j)

# Separate the real and imaginary parts of z
x = np.real(z)
y = np.imag(z)

# Set up the figure and axis with a larger size for higher resolution
fig, ax = plt.subplots(figsize=(12, 12))  # Increase figure size
ax.set_aspect('equal')
ax.set_facecolor('#404345')
ax.grid(False)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)

# Initialize a line object on the plot with a suitable line width for visibility
line, = ax.plot([], [], color='white', linewidth=2)  # Increase linewidth for better visibility

def init():
    """Initialize the animation with an empty line."""
    line.set_data([], [])
    return line,

def update(frame):
    """Update the animation by extending the line to the current frame."""
    line.set_data(x[:frame], y[:frame])
    return line,

# Number of frames corresponds to the length of the x and y data
num_frames = len(x)  # Ensure the animation covers all calculated points

# Create the animation object
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

# Specify FFmpeg as the writer with high quality settings

# Save the animation with high quality
#ani.save(r'E:\Windows Daily Usage\Desktop\coso.mp4', writer='ffmpeg', fps=60, bitrate=5000)

# Display the plot
plt.show()

#print("The video was successfully created and saved.")
#except Exception as e:
#print(f"Failed to save the video: {e}")