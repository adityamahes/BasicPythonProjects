import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.countdown()
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
count = 0
all_cars = []
level = 0
while game_is_on:
    scoreboard.update_scoreboard(level + 1)
    time.sleep(0.1)
    screen.update()
    count += 1
    if count % 6 == 0:
        new_car = CarManager(level)
        all_cars.append(new_car)
    for car in all_cars:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
    if player.is_at_finish():
        level += 1
        player.back_to_start()
        time.sleep(1)
        for car in all_cars:
            car.increment_speed()
scoreboard.game_over()

screen.exitonclick()
