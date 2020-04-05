#!/usr/bin/env python
# -*- coding:utf-8 -*-
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - quit the game
        ''')
    elif command == "quit":
        break
    else:
        print("The command is not exist!")