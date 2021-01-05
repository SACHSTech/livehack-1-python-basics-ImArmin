'''
-------------------------------------------------------------------------------------------
Name: problem2.py
Purpose: Write a program that determines how many pieces of chicken each student will get and how many pieces Mr. Fabroa will get.

Author: Armin

Created: date 2020-12-07
-------------------------------------------------------------------------------------------
'''

print(" Popeyes Chicken Distributor ")

#get number of students in Mr. Fabroa's class
students = int(input("Enter the number of students in Mr. Fabroa's class: "))
#get number of pieces of chicken
chicken = int(input("Enter the number of pieces of chicken to distribute: "))

# compute the chicken distribution for students
pieces_for_each_student = chicken//students
# compute the chicken distribution for teacher
pieces_for_teacher = chicken%students

# output the amount of pieces each student and teacher gets
print("The amount of pieces each student will get is " + str(pieces_for_each_student) + " and the amount of pieces the teacher will get is " + str(pieces_for_teacher))