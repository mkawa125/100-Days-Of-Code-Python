import random

names = 'Dahabu,Juma,Mkawa,Saidi,Hamisi,Neema'
user_list = names.split(',')

random_name = random.choice(user_list)

print(f'{random_name} is going to by the meal today')
