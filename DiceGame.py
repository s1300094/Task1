import random

sum = 0

print("What is your name?")
name = input()
print(f"Hello, {name}!")

print("Rolling dice...")

rand = random.randint(1, 6)
sum += rand
print(f"Die 1: {rand}")

rand = random.randint(1, 6)
sum += rand
print(f"Die 2: {rand}")

print(f"Total value: {sum}")

if sum > 7:
    print("You won!")
else:
    print("You lost!")