# This is a sample Python script.
import random
import Day4_Randomization.module

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

random_int = random.randint(1, 10)
random_float = random.random()
random_uniform = random.uniform(0, 5)

print(random_int)
print(Day4_Randomization.module.pi)
print(random_float)
print(random_uniform)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
