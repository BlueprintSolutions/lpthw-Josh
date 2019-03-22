cars = 100 #This is the total number of cars
space_in_a_car = 4 #this is the total amount of spaces in the car
drivers = 30 #Ths is the total drivers available
passengers = 90 # this is the total number of passengers
cars_not_driven = cars - drivers # this determins the number of cars that are not cars_driven
cars_driven = drivers # this determines the number of cars that are driven
carpool_capacity = cars_driven * space_in_a_car #This determines how much space there is across all the cars being driven.
#'carpool_capacity' is not defined = that when originally writing the document that name of 'carpool_capacity' was not defined with any data it would be like to # line 7 in this code.
average_passengers_per_car = passengers / cars_driven #This determines how many passengers need to be put in each car.



print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "Empty carts today.")
print("We can transport", carpool_capacity, "people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


#Study Drills
#1. I used 4.0 for 'space_in_a_car',but it's that necessar? What happens if it's just 4?
# due to using python 3.7 there is no change

#2. remember that 4.0 is a 'floating point' number. it's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.

#3 write comments about each of the variable assignements.
