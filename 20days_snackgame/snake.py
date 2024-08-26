from turtle import Turtle

STARTUNG_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    #뱀 몸통만들기
    for postion in STARTUNG_POSITION:
      self.add_segment(postion)

  def add_segment(self, position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

  def extend(self):
    self.add_segment(self.segments[-1].position()) #-1은 배열의 맨끝에 값

  def move(self):
    #뱀 움직이기
    for seg_num in range(len(self.segments) - 1, 0, -1):  #3번째 네모 부터 움직이기 시작
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:  #뱀은 반대방향으로 이동 X
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
