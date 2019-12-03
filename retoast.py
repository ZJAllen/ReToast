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

fig = plt.figure()

plt.style.use('fivethirtyeight')
plt.xlim([0, 250])
plt.ylim([0, 250])

plt.plot(temp.x, temp.y, label='Target Temperature')
plt.plot(currentTemp.x, currentTemp.y, label='Current Temperature')
plt.legend(loc=(1.04, 0.5))

plt.tight_layout()
plt.show()

startTime = time.time()

for i in range(0, temp.x[-1], 1):
    elapsedTime = int(time.time() - startTime)
    currentTemp.x.append(elapsedTime)

    tempC = max31855.temperature
    currentTemp.y.append(tempC)

    fig.canvas.draw()
    fig.canvas.flush_events()

    time.sleep(1)


def animate(i):
    elapsedTime = int(time.time() - startTime)
    currentTemp.x.append(elapsedTime)

    tempC = max31855.temperature
    currentTemp.y.append(tempC)

    plt.cla()
    plt.tight_layout()
    plt.plot(temp.x, temp.y, label='Target Temperature')
    plt.plot(currentTemp.x, currentTemp.y, label='Current Temperature')


#ani = FuncAnimation(plt.gcf(), animate, interval=1000)




'''
while True:
    tempC = max31855.temperature
    elapsedTime = int(time.time() - startTime())
    print(f'Temperature: {tempC} C')
    time.sleep(2.0)
'''
