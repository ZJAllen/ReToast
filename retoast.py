import time
import board
import busio
import digitalio
import adafruit_max31855
from temp_profile import SMD291AX as temp
import matplotlib.pyplot as plt


class CurrentTemp():
    x = []
    y = []


currentTemp = CurrentTemp()

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line0, = ax.plot(temp.x, temp.y, label='Target Temperature')
line1, = ax.plot(currentTemp.x, currentTemp.y, label='Current Temperature')

plt.style.use('fivethirtyeight')
plt.xlim([0, 250])
plt.ylim([0, 250])
plt.legend(loc=(1.04, 0.5))
plt.tight_layout()

startTime = time.time()

for i in range(0, temp.x[-1], 1):
    elapsedTime = int(time.time() - startTime)
    currentTemp.x.append(elapsedTime)

    tempC = max31855.temperature
    currentTemp.y.append(tempC)

    print(f'X: {currentTemp.x[-1]}, Y: {currentTemp.y[-1]}')
    
    line1.set_xdata(currentTemp.x)
    line1.set_ydata(currentTemp.y)
    fig.canvas.draw()
    fig.canvas.flush_events()

    time.sleep(1)
