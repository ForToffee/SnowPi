# by Carl Monk (@ForToffee)
# github.com/fortoffee

from time import sleep
from datetime import datetime 
from gpiozero import LED, LEDBoard

board = LEDBoard(9, 22, 8, 18, 7, 17, 23, 24, 25)

def setDay(day):
	board.off()
	sleep(0.25)
	sixDayCount = int((day - 1) / 6)

	for i in range(0, sixDayCount + 1):
		if i > 0:
			if i < 4:
				board.leds[i + 5].on()
				for x in range(0, 6):
					board.leds[x].off()
			else:
				board.blink(on_time=0.5,off_time=0.5)
				break	#don't continue, we're at 25th or greater
			
			
		if i < sixDayCount:
			dayCount = 6
		else:
			dayCount = day - (i * 6)
				
		for x in range(0, dayCount):
			board.leds[x].on()
			sleep(0.25)

			
startup = False
if startup:
	for day in range(1, 26):
		setDay(day)
		sleep(1)

refreshTime = 60*5	#secs - how often to recheck the date and show the current advent day
while True:
	setDay(datetime.today().day)	
	sleep(refreshTime)
