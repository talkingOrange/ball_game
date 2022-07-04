import turtle
import random

def drawit(x,y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

def ball(x):
    ball_pen.write("불꽃 슛!!!!!!!!!!")
    ball_pen.penup()
    ball_pen.goto(x,0)
    ball_pen.pendown()
        

x_value=130

fail=0

drawit(80,300)
turtle.write("중간 결과:")


for i in range(5):
   keeper_pen = turtle.Turtle()
   ball_pen = turtle.Turtle()
   screen = turtle.Screen()
   score = turtle.Turtle()
   middlescore_pen = turtle.Turtle()
   end = turtle.Turtle()
 
   left_img = "image\\left.gif"
   right_img = "image\\right.gif"
   center_img = "image\\center.gif"
   ball_img = "image\\ball.gif"

   screen.addshape(left_img)
   screen.addshape(right_img)
   screen.addshape(center_img)
   screen.addshape(ball_img)

   keeper_pen.shape(center_img)       # 가운데를 막는 골키퍼 그리기
#keeper_pen.shape(left_img)        # 왼쪽을 막는 골키퍼 그리기
#keeper_pen.shape(right_img)       # 오른쪽을 막는 골키퍼 그리기

 
   ball_pen.shape(ball_img)           # 볼 그리기
 

   ball_pen.penup()
   ball_pen.goto(0, -250)
   ball_pen.down()



   option=[left_img,right_img, center_img]


   computer_choice = random.choice(option)     #컴퓨터 골키퍼 랜덤으로 움직임 


#####키퍼에게 움직임 받기##### 

   s= turtle.textinput("","왼쪽으로 차려면 'l', 오른쪽으로 차려면 'r', 중앙으로 차려면'c'를 누르세요.")  



   keeper_pen.shape(computer_choice)


#####키퍼가 l,r,c를 입력 할 경우##### 

   if s == "l":
    ball(-165)

   elif s == "r":
    ball(165)
    
   elif s == "c":
    ball(0)

########################

#####ox 판단하기#####

   if s == "l":
        
          if computer_choice == left_img:
            score="x"
            fail=fail+1

          
          elif computer_choice == right_img :
            score="o"
          else:
            score="o"

            
   elif s == "r":
            
          if computer_choice == right_img:
            score="x"
            fail=fail+1
            
          else:
            score="o"


   elif s == "c":

          if computer_choice == center_img:
            score="x"
            fail=fail+1

          else:
            score="o"
            
#############################   


   middlescore_pen.up()
   middlescore_pen.goto(x_value,300)
   middlescore_pen.write(score)
   x_value+=8
  
   drawit(80,300)
   turtle.write("중간 결과:")

        

 #print(score)             #확인용!!!


#####마지막#####

screen.clear()

n = turtle.textinput("THE END","결과를 확인하시겠습니까?(예:0, 아니요:1)")
if n == "0":
    if fail >= 3:
            end.write("승부차기에 실패하셨습니다:)")
    else:
            end.write("승부차기에 성공하셨습니다:)")
elif n == "1":
            end.write("승부차기를 종료합니다:)")


