print("How old are you?", end=' ')
age = int(input())
print(">>>> age=", repr(age)) #repr is a great way to debug code and see how python is reading the data.
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


#form 2 test

applicant = input("Enter the applicant's name: ")
interviewer = input("Enter the interviewers name: ")
time = input("Enter the appointment time: ")

print(f"{interviewer}, will interview, {applicant} at {time}.")
print(f"{applicant} is {age} old, {height} tall and {weight} heavy. {applicant} will have a meeting with {interviewer} at {time} today.")
