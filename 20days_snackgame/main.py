from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scroeboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scroeboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # 먹이를 먹을때
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  # 벽에 부딪쳤을때 게임 오버
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor(
  ) > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

  # 꼬리와 충돌
  # 머리가 몸통에 닿으면 게임오버
  for segment in snake.segments[1:]: #배열에서 첫번째꺼 제외
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
