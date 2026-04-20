# Second Project: Started at 08:12 AM. Mon, April, 20, 2026. (Note: This is a Beginners Work! I am open to constructive criticism and some tips. THANK YOU!!!)

import time

name = input("What is your name? ")

time.sleep(1)
print(f"Hello {name}! I am Ora's WIP.")

time.sleep(1)
birth_year = input("Which year were you born? ")
age = 2026 - int(birth_year)

time.sleep(0.5)
confirmation = input(f"So, you are {age} years old, correct? (yes/no): ")

if confirmation.strip().lower() == "yes":
    time.sleep(0.5)
    print("Yey! I guessed it. Hehe.")
else:
    time.sleep(2)
    print("Oh no... I might need a software update, huhu... I am so sorry!")
