def cheese_and_crackers(cheese_count, boxes_of_crackers, crackers): #defines the new script written for cheese and crackers
    print(f"You have {cheese_count} cheeses!") #Shows the text inside the brackets on screen for each time we call the script
    print(f"you have {boxes_of_crackers} boxes of crackers") #Shows the text inside the brackets on screen for each time we call the script
    print(f"you have {crackers} crackers") #added to function #Shows the text inside the brackets on screen for each time we call the script
    print("Man that's enough for a party!") #Shows the text inside the brackets on screen for each time we call the script
    print("Get a blanket.\n") #Shows the text inside the brackets on screen for each time we call the script


print("We can just give the fucntion numbers directly:") #Shows the text inside the brackets on screen
cheese_and_crackers(20, 30, 10) # defines cheese_count as 20, boxes_of_crackers as 30 and crackers as 10 then prints it out using the script above.


print("OR, we can use variables from our script:") #Shows the text inside the brackets on screen
amount_of_cheese = 10 #defines amount_of_cheese as 10 for the script above
amount_of_crackers = 50 #defines amount_of_crackers as 50 for the script above
crackers = 12 #defines the variable crackers as 12 for the script above

cheese_and_crackers(amount_of_cheese, amount_of_crackers, crackers) # calls the cheese_and_crackers script and passes the variales similar to the argv script


print("We can even do math inside too:") #Shows the text inside the brackets on screen
cheese_and_crackers(10 + 20, 5 + 6, 0 + 4) # calls the cheese_and_crackers script and passes the variales similar to the argv script


print("And we can combine the two, variables and math:") #Shows the text inside the brackets on screen
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000, crackers + 2) # calls the cheese_and_crackers script and passes the variales similar to the argv script

#1
print("1. And we can play with cheese and crackers as much as we want")
cheese_and_crackers(amount_of_cheese + 100 * 20, amount_of_crackers * 0, crackers * 4)

#2
print("2. What else can I do with a function?")
amount_of_cheese = amount_of_crackers + (crackers * 4 + 2)
cheese_and_crackers(amount_of_cheese, amount_of_crackers, crackers)

#3
print("3. Another Function")
cheese_and_crackers(1,2,3)

#4
print("4. What to do?")
cheese_and_crackers("-", "+", "*")

#5
print("5. What could be next?")
amount_of_cheese = int(10 +  50 + 6 * amount_of_crackers * crackers)
amount_of_crackers = int(amount_of_cheese / crackers)
crackers = amount_of_cheese == amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers, crackers)

#6
print("6. yummy")
crackers != amount_of_crackers
cheese_and_crackers((1+3+4*12),"456",crackers)

#7
print(f"7. MMMM {crackers} for me :) ")
crackers = (f" {crackers} my name is what?")
amount_of_crackers = "my name"
cheese_and_crackers((6==6), crackers, amount_of_crackers)

#8
print("8. Keep it easy")
cheese_and_crackers(1,"help", 567)

#9
print("9. next")
amount_of_cheese = input("Is the Cheese true or false? ")
if amount_of_cheese == ("false"):
    print("that's false!")
    amount_of_cheese = "false2"

elif amount_of_cheese == ("true"):
    print("that's true!")
    amount_of_cheese = "true2"

cheese_and_crackers(1, 2, amount_of_cheese)

#10
print("10. Ready for the big finally")
if amount_of_cheese == crackers:
    amount_of_cheese = crackers + (1 * 2)
    cheese_and_crackers(1, 4, amount_of_cheese)

elif amount_of_cheese != crackers:
    amount_of_cheese = crackers + str(212)
    amount_of_cheese = 3
    cheese_and_crackers(1, amount_of_cheese, amount_of_crackers)
