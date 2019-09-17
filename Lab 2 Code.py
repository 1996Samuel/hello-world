#Input user's name
name = input('Enter your name:\n')

#Ask questions
creditsdone = int(input('How many credits have you completed?\n'))
creditsrequired = int(input('How many credits do you need to complete your degree?\n'))
typicalcredits = int(input('How many credits do you typically take per semester?\n'))

#Calculate time till graduation
timetillgrad = (creditsrequired - creditsdone)/typicalcredits

#round up
import math
TTGrounded = math.ceil(timetillgrad)

print(name, 'you have', TTGrounded, 'semesters until you can graduate')