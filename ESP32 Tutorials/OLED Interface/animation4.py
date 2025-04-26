import time
import math
from machine import Pin, I2C
import ssd1306

# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Create OLED object
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Function to draw a circle
def draw_circle(x_center, y_center, radius):
    for angle in range(0, 360, 1):
        x = int(x_center + radius * math.cos(math.radians(angle)))
        y = int(y_center + radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)

# Function to draw a sine wave
def draw_sine_wave(offset):
    for x in range(0, 128):
        y = int(32 + 20 * math.sin((x + offset) / 10))
        oled.pixel(x, y, 1)

# Animation loop
x, y = 64, 32  # Initial position of the circle
radius = 10     # Radius of the circle
dx, dy = 2, 2   # Speed of movement in x and y directions
sine_offset = 0  # Offset for sine wave animation

while True:
    oled.fill(0)  # Clear the display

    # Draw the moving sine wave
    draw_sine_wave(sine_offset)

    # Draw the bouncing circle
    draw_circle(x, y, radius)

    # Show the graphics
    oled.show()

    # Move the circle
    x += dx
    y += dy

    # Bounce the circle off the edges of the screen
    if x + radius >= 128 or x - radius <= 0:
        dx = -dx  # Reverse the x direction
    if y + radius >= 64 or y - radius <= 0:
        dy = -dy  # Reverse the y direction

    # Update sine wave offset for animation
    sine_offset += 1

    # Control the speed of the animation
    time.sleep(0.03)
