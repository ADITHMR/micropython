from machine import Pin, I2C   
import ssd1306
import time



i2c = I2C(0, scl=Pin(22), sda=Pin(21))


print("I2C scan:", i2c.scan())  


oled = ssd1306.SSD1306_I2C(128, 64, i2c)



oled.fill(0)
oled.text("Robo Ninjaz!", 0, 0)

for i in range(50):
    oled.fill_rect(50, 30, 25, 10, 0)
#     oled.show()
#     oled.show()
    oled.text(str(i), 50, 30)
    time.sleep(1)
    oled.show()






oled.show()