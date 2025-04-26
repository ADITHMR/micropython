import time
import math
from machine import Pin, I2C
import ssd1306

# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Create OLED object
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Parameters for the bouncing ball and circle
center_x = 64  # Center of the circle
center_y = 32  # Center of the circle
radius = 20    # Radius of the circle (boundary)
ball_radius = 3  # Radius of the ball
angle = 0       # Initial angle of the ball
ball_x = 64     # Initial x position of the ball
ball_y = 32     # Initial y position of the ball
speed_x = 1     # Speed of the ball in x direction
speed_y = 1     # Speed of the ball in y direction

# Function to draw the circle (boundary)
def draw_circle():
    oled.fill(0)  # Clear the screen
    for angle in range(0, 360, 2):  # Draw the circle with steps of 2 degrees
        x = int(center_x + radius * math.cos(math.radians(angle)))
        y = int(center_y + radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)

# Function to draw the ball
def draw_ball(x, y):
    oled.fill_rect(x - ball_radius, y - ball_radius, 2 * ball_radius, 2 * ball_radius, 1)

# Animation loop
while True:
    # Draw the circle boundary
    draw_circle()

    # Draw the ball at the current position
    draw_ball(ball_x, ball_y)

    # Update the ball's position
    ball_x += speed_x
    ball_y += speed_y

    # Check for collision with the boundary and reverse direction if necessary
    if (ball_x - ball_radius) <= (center_x - radius) or (ball_x + ball_radius) >= (center_x + radius):
        speed_x = -speed_x  # Reverse direction in x

    if (ball_y - ball_radius) <= (center_y - radius) or (ball_y + ball_radius) >= (center_y + radius):
        speed_y = -speed_y  # Reverse direction in y

    # Update the display
    oled.show()

    # Control the speed of the animation
    time.sleep(0.03)  # Adjust this to control speed of the ball
