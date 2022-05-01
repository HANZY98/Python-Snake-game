# Importing curses, allows us to use keys
import curses as mykeys

from random import randint as myrandomiser

# Initialising setup window
mykeys.initscr();
window = mykeys.newwin(20, 60, 0, 0);
window.keypad(1);
mykeys.noecho();
mykeys.curs_set(0);
window.border(0);
window.nodelay(1);

#Snake creation and food creation
mySnake = [(4,10), (4,9), (4,8)];
myFood = (10, 20);

window.addch(myFood[0], myFood[1], '*' );
#game operations and logic
gameScore = 0;

escape = 27;
pressedKeys = mykeys.KEY_RIGHT

while pressedKeys != escape:

  window.addstr(0, 2, "Score" + str(gameScore) + " ");
  window.timeout(150 - (len(mySnake)) // 5 + len(mySnake)//10 % 120)

  other_key = pressedKeys
  myEvent = window.getch();
  pressedKeys = myEvent if myEvent != -1 else other_key

  if pressedKeys not in [mykeys.KEY_RIGHT, mykeys.KEY_LEFT, mykeys.KEY_DOWN, mykeys.KEY_UP, escape]:
    pressedKeys = other_key

  x = mySnake[0][0]
  y = mySnake[0][1]

  if pressedKeys == mykeys.KEY_DOWN:
    x += 1
  if pressedKeys == mykeys.KEY_UP:
    x -= 1
  if pressedKeys == mykeys.KEY_LEFT:
    y -= 1
  if pressedKeys == mykeys.KEY_RIGHT:
    y += 1

  mySnake.insert(0, (x, y))

  if x == 0: break
  if x == 19: break
  if y == 0: break
  if y == 59: break

  if mySnake[0] in mySnake[1:]:break

  if mySnake[0] == myFood:
    gameScore += 1
    myFood = ()
    while myFood == ():
      myFood = (myrandomiser(1,18), myrandomiser(1,58))
      if myFood in mySnake:
        myFood = ()
    window.addch(myFood[0], myFood[1], '*' )
  else:
    myLast = mySnake.pop()
    window.addch(myLast[0], myLast[1], " ")

  window.addch(mySnake[0][0], mySnake[0][1], '=' );

mykeys.endwin();
print("This is the Final Score = {gameScore}");


