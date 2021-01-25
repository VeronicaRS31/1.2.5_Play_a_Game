#Hangman Game
# import list of words, import random module, import turtle module
import random
from words import word_list
import turtle as trtl 


#turtle screen set up, background color of screen is yellow
wn= trtl.Screen()
wn.bgcolor("yellow")
#creation of turtles
screen_writer= trtl.Turtle()
hangman_painter= trtl.Turtle(shape="turtle")
tries_counter= trtl.Turtle(shape="arrow")
counter= trtl.Turtle(shape="arrow")

# screen_writer turtle writes the title on the screen 
screen_writer.hideturtle()
screen_writer.penup()
screen_writer.goto(-120,250)
font_setup = ("Arial", 30, "normal")
screen_writer.write("Hangman Game", font=font_setup)
hangman_painter.fillcolor("purple")
timer = 300
counter_interval = 3500  #1000 represents 1 second
timer_up = False

#hangman_drawer draws the pole for the hangman function
def draw_hang():
  hangman_painter.setheading(0)
  hangman_painter.pencolor("black")
  hangman_painter.pensize(2)
  hangman_painter.penup()
  hangman_painter.goto(-150,-300)
  hangman_painter.pendown()
  hangman_painter.left(90)
  hangman_painter.forward(450)
  hangman_painter.right(90)
  hangman_painter.forward(300)

draw_hang()
#counter and tries_counter turtles go to designated spots
counter.penup()
counter.goto(-400,300)
tries_counter.penup()
tries_counter.goto(400,300)
# functions to draw the hangman in steps

def draw_face():
  hangman_painter.pd()
  hangman_painter.pencolor("purple")
  hangman_painter.penup()
  hangman_painter.goto(150,50)
  hangman_painter.pd()
  hangman_painter.circle(50)

def draw_body():
  hangman_painter.right(90)
  hangman_painter.forward(200)

def draw_left_leg():
  hangman_painter.right(45)
  hangman_painter.forward(100)

def draw_right_leg():
  hangman_painter.backward(100)
  hangman_painter.left(90)
  hangman_painter.forward(100)

def draw_left_arm():
  hangman_painter.backward(100)
  hangman_painter.right(225)
  hangman_painter.forward(100)
  hangman_painter.left(45)
  hangman_painter.forward(100)

def draw_right_arm():
  hangman_painter.backward(100)
  hangman_painter.right(90)
  hangman_painter.forward(100)

def draw_eyes():
  hangman_painter.right(45)
  hangman_painter.penup()
  hangman_painter.goto(130,100)
  hangman_painter.begin_fill()
  hangman_painter.circle(5)
  hangman_painter.end_fill()
  hangman_painter.pu()
  hangman_painter.forward(35)
  hangman_painter.begin_fill()
  hangman_painter.circle(5)
  hangman_painter.end_fill()

def draw_smile():
  hangman_painter.pu()
  hangman_painter.goto(120,80)
  hangman_painter.pd()
  hangman_painter.forward(50)


# different stages for the hangman to appear

stage=0
def hang(i):
  global stage
  if stage==0:
    draw_face()
  elif stage ==1:
    draw_body()
  elif stage ==2:
    draw_left_leg()
  elif stage ==3:
    draw_right_leg()
  elif stage ==4:
    draw_left_arm()
  elif stage ==5:
    draw_right_arm()
  elif stage ==6:
    draw_eyes()
  elif stage ==7:
    draw_smile()
  stage +=1


# function that gets a word for the player to get of the list of words created in a different file
def get_word():
  word= random.choice(word_list)
  return word.upper()

# timer function for the game

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  elif guessed== True:
    timer_up== True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


# the elements in the screen to dissapear function after game is over
def time_down():
  screen_writer.clear()
  hangman_painter.clear()
  counter.clear()
  tries_counter.clear()

# whole hangman game, with if/elif/else/ while loop staments
def play(word):
  word_completion = "_" * len(word) #variable that checks if the player gets word right
  global guessed 
  guessed= False # checks to see if the guess is right for the word
  guessed_letters=[] # empty list to keep already guessed incorrect letters
  guessed_words=[] # empty list to keep already guessed words
  tries= 8 # the amount of tries the player has
  screen_writer.pu()
  screen_writer.goto(-120,250)
  screen_writer.pd()
  screen_writer.clear()
  screen_writer.write("Let's play hangman", font=font_setup) # writes lets play hangman on screen
  counter.hideturtle()
  counter.write("timer: ", font= font_setup) # writes timer on the screen
  tries_counter.hideturtle()
  tries_counter.write("tries: ",font=font_setup) # writes tries and the number of tries the player has
  tries_counter.pu()
  tries_counter.goto(500,300)
  tries_counter.pd()
  tries_counter.write(tries,font=font_setup )
  print(word_completion)

# writing the letter


# loop/ if/ else statements for the hangman game
  while not guessed and tries > 0 and timer_up== False: 
    countdown() # starts the timer for the game
    guess= input("Please guess a letter or word: ").upper() # gets letter/word input from player
    if len(guess)== 1 and guess.isalpha():
      if guess in guessed_letters:
        print("you have already guessed this letter", guess) # if they have already guessed that guess already 
      elif guess not in word: # if letter is wrong store in wrong letter list
        guessed_letters.append(guess)
        print(guess, "is not in the word")
        tries -= 1 # lives minus 1
        hang(stage) # draw the hang stage correspondenly
        tries_counter.clear()
        tries_counter.hideturtle()
        tries_counter.pu()
        tries_counter.goto(400,300)
        tries_counter.write("tries: ",font=font_setup)
        tries_counter.pu()
        tries_counter.goto(500,300)
        tries_counter.pd()
        tries_counter.write(tries,font=font_setup )
      else: # if letter or word guessed then do this
        print("good job", guess, "is in the word")
        guessed_letters.append(guess)
        word_as_list= list(word_completion)
        indices= [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index]= guess
        word_completion= "". join(word_as_list)
        if "_" not in word_completion:
          guessed = True
    elif len(guess)== len(word) and guess.isalpha():# if word already guessed
      if guess in guessed_words:
        print("you have already guessed the word", guess)
      elif guess!= word:
        guessed_words.append(guess)
        print(guess,"is not the word")
        tries -=1
        hang(stage)
        tries_counter.clear()
        tries_counter.hideturtle()
        tries_counter.pu()
        tries_counter.goto(400,300)
        tries_counter.write("tries: ",font=font_setup)
        tries_counter.pu()
        tries_counter.goto(500,300)
        tries_counter.pd()
        tries_counter.write(tries,font=font_setup )
      else: # if guess is correct then guessed turns true
        guessed= True
        word_completion= word

    else: # if none of the above then print not the right guess
      print("not the right guess")
  if guessed== True: # if guess is true then print congrats guess is right and shut down the game
    print("congrats, you guessed the right word!, "+ word)
    time_down()
  elif timer_up== True: # if timer up then turn of the game
    time_down()
    print("sorry time's up, but the correct word was, " +word)
  else: # if none of the above becomes true and the # of tries is 0 then print sorry you lost and the correct word
    print("sorry you ran out of tries, the word was " + word+ " Maybe next time")

# gets all the functions together to create game
def main():
  word = get_word()
  play(word)

# repeats the game if user says yes
''''
  if input("Play Again? (Y/N)").upper() == "Y":  # this repeats the game if the player wants to play again
    tries_counter.clear()
    hangman_painter.clear()
    timer_up == False
    global stage
    stage=0
    global timer
    timer==300
    draw_hang()
    word = get_word()
    play(word)

'''


main()

wn.mainloop()



