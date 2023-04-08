name = ('John Smith')
height = 1.87
weight = 102
bmi = weight / (height * height)

line1 = (f'{name} is {height} meters tall,')
line2 = (f'weighs {weight} kilograms, and his BMI is:')
line3 = f'{bmi:.2f}'

print(line1)
print(line2)
print(line3) 