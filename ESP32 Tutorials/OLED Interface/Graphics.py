import time
import math
from machine import Pin, I2C
import ssd1306

# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Create OLED object
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the screen
oled.fill(0)
oled.show()
while True:
    # Draw a rectangle
    oled.rect(10, 10, 50, 30, 1)
    oled.show()
    time.sleep(1)

    # Draw a filled rectangle
    oled.fill_rect(70, 10, 50, 30, 1)
    oled.show()
    time.sleep(1)
    oled.fill(0) 
    # Draw a circle (Using pixels in a loop to create a circle)
    def draw_circle(x_center, y_center, radius):
        for angle in range(0, 360, 1):
            x = int(x_center + radius * math.cos(math.radians(angle)))
            y = int(y_center + radius * math.sin(math.radians(angle)))
            oled.pixel(x, y, 1)

    # Draw a circle
    draw_circle(64, 32, 20)
    oled.show()
    time.sleep(1)

    # Draw a filled circle (using a similar approach but filling the interior)
    def fill_circle(x_center, y_center, radius):
        for r in range(radius):
            draw_circle(x_center, y_center, r)

    # Draw a filled circle
    fill_circle(64, 32, 10)
    oled.show()
    time.sleep(1)

    # Draw a line
    oled.line(0, 0, 127, 63, 1)  # Diagonal line
    oled.show()
    time.sleep(1)
    
    # Draw a sine wave pattern
    oled.fill(0)  # Clear the screen again
    for x in range(0, 128):
        y = int(32 + 20 * math.sin(x / 10))
        oled.pixel(x, y, 1)  # Plot sine wave points
        oled.show()
        time.sleep(.01)
    oled.show()
    time.sleep(2)

    # Clear the display and end
    oled.fill(0)
    oled.show()
