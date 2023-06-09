import random

sum = 0

print("Rolling dice...")

rand = random.randint(1, 6)
sum += rand
print(f"Die 1: {rand}")

rand = random.randint(1, 6)
sum += rand
print(f"Die 2: {rand}")

print(f"Total value: {sum}")
