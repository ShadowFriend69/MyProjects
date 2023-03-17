import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("My Crossin' road Game Game")
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=tim.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if tim.ycor() > 280:
        tim.new_level()
        car_manager.car_speed_up()
        scoreboard.current_level()

    # Collide with a car
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
