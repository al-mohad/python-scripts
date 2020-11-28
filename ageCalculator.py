import datetime

birth_year = input('What year were you born? ')
current_year = datetime.datetime.now().year
age = current_year - int(birth_year)
print(f'Your are {age} years old.')