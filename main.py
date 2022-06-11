#
#   _____       _                      _           _   _           _    __      ____  __ 
#  / ____|     | |                    | |         | | | |         | |   \ \    / /_ |/_ |
# | |  __  __ _| |__   ___  ___    ___| |__   __ _| |_| |__   ___ | |_   \ \  / / | | | |
# | | |_ |/ _` | '_ \ / _ \/ __|  / __| '_ \ / _` | __| '_ \ / _ \| __|   \ \/ /  | | | |
# | |__| | (_| | |_) |  __/\__ \ | (__| | | | (_| | |_| |_) | (_) | |_     \  /   | |_| |
#  \_____|\__,_|_.__/ \___||___/  \___|_| |_|\__,_|\__|_.__/ \___/ \__|     \/    |_(_)_|
#


# Setup for cleanr looking text dont mind this
from os import system as sys
# For other projects
#from os import environ as env
#from time import sleep as wait
def clear(): sys('clear')

name = 'UNKNOWN USER'
# User Regestration
print('Hello', name + '! Lets get you registred!')
print('Whats your name?')
name = input('>>> ')
# Game selection
clear()
print('Welcome' , name)
print('Whats is your favorte game?')
gname = input('>>> ')

# React based on game
if(gname == 'Minecraft'):
  clear()
  print('Mine too!')
  print('Whats your favorite thing about minecraft?')
  favmc = input('>>> ')
  # If the sculk is their favorite thing then they get scammed
  if(favmc == 'sculk'):
    clear()
    print('No way! Me too' , name + '! We have so mutchin common!')
    print('Sayyyy, do you want to fill out a quick form?')
    quiz = input('[Y/N (caps)]>>> ')
    # Scam
    if(quiz == 'Y'):
      clear()
      input('Credit Card: ')
      input('3-didget credit card pin: ')
      input('Name On Credit Card: ')
      print('Haha thx for ur info noob')
      print(' ')
      print('Ending: scammed')
    # If they say no
    elif(quiz == 'N'):
      print('Oh well, sorry I have to go, nice talking to ya!')
      print(' ')
      print('Ending: awkward')
      exit
  # If sculk is NOT the favorite thing
  else:
    clear()
    print('Oh well my favorite is sculk')
    print('Well it was nice meeting you!')
    print(' ')
    print('Ending: not that mutch in common')
    exit
# If minecraft is not the game selected
else:
  print('Oh, I like Minecraft but I guess' , gname , 'is good too.')
  print(' ')
  print('Ending: ???')




