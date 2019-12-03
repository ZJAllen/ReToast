import time
import board
import busio
import digitalio
import adafruit_max31855
from temp_profile import SMD291AX as temp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CurrentTemp():
    x = []
    y = []

currentTemp = CurrentTemp()

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)

plt.style.use('fivethirtyeight')
plt.xlim([0, 250])
plt.ylim([0, 250])
 
plt.plot(temp.x, temp.y, label='Target Temperature')

startTime = time.time()


def animate(i):
    elapsedTime = int(time.time() - startTime())
    currentTemp.x.append(elapsedTime)
    
    tempC = max31855.temperature
    currentTemp.y.append(tempC)

    plt.cla()
    plt.plot(currentTemp.x, currentTemp.y, label='Current Temperature')


ani = FuncAnimation(plt.gfc(), animate, interval=1000)

plt.legend(loc=(1.04, 0.5))
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.tight_layout()
plt.show()


'''
while True:
    tempC = max31855.temperature
    elapsedTime = int(time.time() - startTime())
    print(f'Temperature: {tempC} C')
    time.sleep(2.0)
'''
