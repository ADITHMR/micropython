import time
import math
from machine import Pin, I2C
import ssd1306

# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Create OLED object
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Parameters for progress bar and rotating indicator
center_x = 64
center_y = 32
radius = 20  # Radius of the circle (progress bar track)
progress_radius = 15  # Radius of the circular progress bar
angle = 0  # Initial angle of the rotating indicator
progress = 0  # Progress percentage (0-100)

# Function to draw the progress bar as a circular arc
def draw_progress_bar(progress):
    oled.fill(0)  # Clear the screen
    # Draw the background circle (track of the progress bar)
    for angle in range(0, 360, 2):  # Draw the background circle in steps of 2 degrees
        x = int(center_x + progress_radius * math.cos(math.radians(angle)))
        y = int(center_y + progress_radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)
    
    # Draw the progress arc
    for angle in range(0, int(3.6 * progress), 2):  # Draw the progress arc based on progress
        x = int(center_x + progress_radius * math.cos(math.radians(angle)))
        y = int(center_y + progress_radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)

# Function to draw the rotating indicator (needle)
def draw_rotating_indicator(angle):
    x_end = int(center_x + radius * math.cos(math.radians(angle)))
    y_end = int(center_y + radius * math.sin(math.radians(angle)))
    oled.line(center_x, center_y, x_end, y_end, 1)

# Animation loop
while True:
    # Update progress value
    progress += 1  # Increment progress
    if progress > 100:
        progress = 0  # Reset the progress after 100%

    # Draw the circular progress bar with the current progress
    draw_progress_bar(progress)

    # Draw the rotating indicator (needle)
    draw_rotating_indicator(angle)

    # Update the display
    oled.show()

    # Increment the angle for the rotating indicator (needle)
    angle += 6  # Move 6 degrees for each frame (this speed can be adjusted)

    # Reset the angle to create a continuous loop for the rotating indicator
    if angle >= 360:
        angle = 0

    # Control the speed of the animation
    time.sleep(0.05)  # Adjust speed of the animation
