# -*- coding: utf-8 -*-
"""
This is a simple draw machine. It tells the user where the meeting will take 
place when there are three locations to choose from. 
It also gives the time of the draw.



"""
import random
import time
print("*" * 15)
print("Test draw")
print("*" * 15)
now = time.strftime("%H:%M:%S")
print("Where will we meet? There are three places to choose from: a forest, a field and a valley.")
time.sleep(3)
print("Initialization of the draw.")
time.sleep(3)
print("The draw is in progress...")
time.sleep(4)
choices = ["a forest", "a field", "a valley"]
score = random.choice(choices)
print("*" * 15)
time.sleep(3)
print(f"The result: {score}. Time of the draw: {now}")