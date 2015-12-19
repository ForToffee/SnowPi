# by Carl Monk (@ForToffee)
# github.com/fortoffee
 
from time import sleep
from datetime import datetime 
from gpiozero import LED, LEDBoard, Button, Buzzer
import random 
 
board = LEDBoard(9, 22, 8, 18, 7, 17, 23, 24, 25)
button = Button(20)
buzzer = Buzzer(21)


def game():
	random.seed()
	board.on()
	sleep(0.5)
	for i in range(8, -1, -1):
		board.leds[i].off()
		sleep(0.5)
	
	gameState = 0	#1 = win, -1 = lose
	led = 0
	while gameState == 0 :
		delay = random.randint(2, 6)
		count = 0
		
		board.leds[led].toggle()
		while count < delay:
			if button.is_pressed:
				if board.leds[led].is_lit:
					count = delay
					led += 1
					if led > 8:
						gameState = 1
						board.blink()
						sleep(5)
						board.off()
					else:
						sleep(0.5)
						board.leds[led].on()
					
					break

				else:
					gameState = -1
					buzzer.beep(n=1,background=False)
					for i in range(led, -1, -1):
						board.leds[i].off()
						sleep(0.5)

					break
			sleep(0.1)
			count += 1


while True:
	board.off()
	while not button.is_pressed:
		for n in range(0,9):
			if button.is_pressed:
				break
			board.leds[n].toggle()
			sleep(0.25)
			
	game()

	
