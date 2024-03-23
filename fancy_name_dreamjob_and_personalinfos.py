#pseudocode

# import pyfiglet
import pyfiglet
# import termcolor
from termcolor import colored
# ask user for inputs
name = input("Please enter your name: ")
dream_job = input("Please enter your dream job: ")
age = int(input("Please enter your age: "))
hometown = input("Please enter your hometown: ")
birthdate = input("Please enter your birthdate: ")
pet_peeves = input("Please enter your Pet peeve: ")
# use pyfiglet to make a sentence_art with the inputs
sentence_art = pyfiglet.figlet_format(f"Hi, my name is {name}, I'm from {hometown}, I was born on {birthdate}, I'm {age} years old, my pet peeve is {pet_peeves} and being a {dream_job} is my dream job", font="roman",width =160)
# print the sentence_art with the use of termcolor

