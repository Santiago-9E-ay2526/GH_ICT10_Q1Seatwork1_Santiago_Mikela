# Seatwork 1
from pyscript import display, document


studentName = 'Mikela Romielle Juliano Santiago' #string
studentAge = 14 #integer
studentHeight1 = 145 #integer
countries_visit = ['France', 'Korea', 'USA'] #list
student_type = False #boolean
funFacts = {'color':'purple', 'car_brand': 'Toyota', 'shoe_size':'36', 'best_friend': 'Guia and Jaena'} #dictionary
favFruits = set(['strawberry', 'pear', 'apple', 'kiwi', 'mango']) #set
daysOfWeek = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') #tuple


display(f'Hello! My name is <i>{studentName}</i>. <br> I am {studentAge} years old. <br> My height is {studentHeight1}cm. <br> The countries I want to visit are {countries_visit}. <br> Am I a new student?: {student_type}. <br> Some things about me: {funFacts}. <br> The fruits I like are {favFruits}. <br> The days of the week are {daysOfWeek}.', target='result')
document.getElementById('result').innerHTML = f'Hello! My name is <i>{studentName}</i>. <br> I am {studentAge} years old. <br> My height is {studentHeight1}cm. <br> The countries I want to visit are {countries_visit}. <br> Am I a new student?: {student_type}. <br> Some things about me: {funFacts}. <br> The fruits I like are {favFruits}. <br> The days of the week are {daysOfWeek}.'