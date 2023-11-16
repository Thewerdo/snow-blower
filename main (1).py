#This animation depicts snow being blown with a snowblower during a Canadian winter. It then snows and coveres everything with snow.

#Initialize Tkinter with these
from tkinter import*
from time import*
from random import*

myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="dark blue")
screen.pack()

#background

#snow
screen.create_rectangle(0, 0, 800, 600, fill="white", outline="white")

#house
screen.create_rectangle(150, 500, 650, 600, fill="brown")
screen.create_line(400, 500, 400, 600)

#very large driveway
screen.create_rectangle(200, 0, 650, 500, fill="grey")

#person start
x1 = 150
y1 = 0

#snow arrays
x = []
y = []
sizes = []
xSpeed = []
ySpeed = []
snow = []

#filling arrays
for i in range (50):
  x.append(105)
  y.append(450)
  xSpeed.append(uniform(-4, -1))
  ySpeed.append(uniform(-4, 4))
  sizes.append(uniform(1, 10))
  snow.append(0)

for i in range (65):
  
  #driveway portion that is revealed by the snow being gone
  screen.create_rectangle(150, 0, 200, y1+180, fill="grey")
  screen.create_line(200, 0, 200, y1+180, fill="grey")
  
  #person
  head = screen.create_oval(x1, y1, x1+50, y1+50, fill="tan")
  hat = screen.create_arc(x1, y1-10, x1+50, y1+40, fill="purple", start=0, extent=180)
  coat = screen.create_line(x1+25, y1+50, x1+25, y1+100, width=5, fill="blue")
  leg1 = screen.create_line(x1+25, y1+100, x1, y1+150)
  pant1 = screen.create_line(x1+25, y1+100, x1+5, y1+145, width=5, fill="green")
  leg2 = screen.create_line(x1+25, y1+100, x1+50, y1+150)
  pant2 = screen.create_line(x1+25, y1+100, x1+45, y1+145, width=5, fill="green")
  arm1 = screen.create_line(x1+25, y1+65, x1, y1+100)
  sleeve1 = screen.create_line(x1+25, y1+65, x1+5, y1+95, width=5, fill="blue")
  arm2 = screen.create_line(x1+25, y1+65, x1+50, y1+100)
  sleeve2 = screen.create_line(x1+25, y1+65, x1+45, y1+95, width=5, fill="blue")

  #snowblower
  handle_main = screen.create_line(x1, y1+100, x1+50, y1+100, width=8)
  handle_side1 = screen.create_line(x1, y1+100, x1, y1+120, width=3)
  handle_side2 = screen.create_line(x1+50, y1+100, x1+50, y1+120, width=3)
  snowblower_arm = screen.create_polygon(x1, y1+140, x1-15, y1+140, x1-25, y1+115, x1-45, y1+115, x1-45, y1+135, x1-30, y1+135, x1-20, y1+160, x1, y1+160, x1, y1+140, fill="red")
  snowblower_main = screen.create_rectangle(x1, y1+120, x1+50, y1+180, fill="red") 
  snowblower_extra = screen.create_oval(x1, y1+120, x1+50, y1+180, fill="red")
  screen.update()
  y1 += 5
  sleep(0.05)
  #not delete scene on last frame
  if i < 64:
    screen.delete(head, hat, coat, leg1, leg2, arm1, arm2, pant1, pant2, sleeve1, sleeve2, handle_main, handle_side1, handle_side2, snowblower_main, snowblower_extra, snowblower_arm)

#make the snow
for i in range (20):
  for j in range (50):
    snow[j] = screen.create_oval(x[j]-sizes[j], y[j]-sizes[j], x[j]+sizes[j], y[j]+sizes[j], fill="white")
    x[j] = x[j] + xSpeed[j]
    y[j] = y[j] + ySpeed[j]

  screen.update()
  sleep(0.05)

  #snow update
  if i != 19:
    for j in range (50):
      screen.delete(snow[j])

sleep(1)

#All done!
screen.create_oval(200, 250, 300, 300, fill="white")
screen.create_text(210, 275, text="All done!", font="Comic 10", fill="black", anchor=W)
screen.update()
sleep(2)
screen.delete('all')

#Change Scene, new anchor point
x1 = 500
y1 = 350
#background

#light sky so that it can turn dark later
sky = screen.create_rectangle(0, 0, 800, 600, fill="light blue", outline="light blue")

#ground
screen.create_rectangle(0, 450, 800, 600, fill="white")
screen.create_rectangle(150, 450, 650, 600, fill="grey")

#house
screen.create_rectangle(200, 250, 600, 450, fill="#BC4A3C")
screen.create_polygon(150, 250, 650, 250, 400, 100, fill="brown")

#door
screen.create_rectangle(500, 350, 550, 450, fill="black")
door = screen.create_rectangle(500, 350, 550, 450, fill="#5D2906")

#pile of snow
screen.create_oval(650, 350, 800, 600, fill="white", outline="white")

#person
head = screen.create_oval(x1, y1, x1+30, y1+30, fill="tan")
hat = screen.create_arc(x1, y1-10, x1+30, y1+20, fill="purple", start=0, extent=180)
coat = screen.create_line(x1+15, y1+30, x1+15, y1+70, width=5, fill="blue")
leg1 = screen.create_line(x1+15, y1+70, x1, y1+100)
pant1 = screen.create_line(x1+15, y1+70, x1+5, y1+95, width=5, fill="green")
leg2 = screen.create_line(x1+15, y1+70, x1+30, y1+100)
pant2 = screen.create_line(x1+15, y1+70, x1+25, y1+95, width=5, fill="green")
arm1 = screen.create_line(x1+15, y1+50, x1, y1+70)
sleeve1 = screen.create_line(x1+15, y1+50, x1+5, y1+65, width=5, fill="blue")
arm2 = screen.create_line(x1+15, y1+50, x1+30, y1+70)
sleeve2 = screen.create_line(x1+15, y1+50, x1+25, y1+65, width=5, fill="blue")
screen.update()

#he goes inside
sleep(1)
screen.delete(door)
screen.update()
sleep(2)
screen.delete(head, hat, coat, leg1, leg2, pant1, pant2, arm1, sleeve1, arm2, sleeve2)
screen.create_rectangle(500, 350, 550, 450, fill="#5D2906")
screen.update()
sleep(2)

#new arrays for new snow
x = []
y = []
xSpeed = []
ySpeed = []
snow = []

#make the snow
for i in range (200):
  x.append(uniform(0, 800))
  y.append(uniform(-2000, 0))
  xSpeed.append(uniform(-1, 1))
  ySpeed.append(uniform(3, 7))
  snow.append(0)

#make it snow
for i in range (1000):
  for j in range (200):
    snow[j] = screen.create_oval(x[j], y[j], x[j]+3, y[j]+3, fill="white", outline="white")
    x[j] = x[j] + xSpeed[j]
    y[j] = y[j] + ySpeed[j]

  #sky goes dark
  if i == 250:
    screen.delete(sky)

  #snow has expanded
  if i == 500:
    screen.create_rectangle(0, 400, 800, 600, fill="white", outline="white")
    screen.create_polygon(150, 250, 150, 200, 400, 50, 650, 200, 650, 250, fill="white", outline="white")
    screen.create_oval(650, 250, 800, 500, fill="white", outline="white")
  screen.update()
  sleep(0.03)
  for j in range (200):
    screen.delete(snow[j])

screen.update()
input()