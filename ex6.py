types_of_people = 10 #defining the number in types of people
x = f"There are {types_of_people} types of people." #Adding a format to the name X

binary = "binary" #definining binary
do_not = "don't" #defining do_not name
y = f"Those who know {binary} and those who {do_not}." #Adding binary and do_not names to a format under the name y

print(x) #shows on the users screen what is typed in x as "There are 10 Types of people.""
print(y) #shows on the users screen what is typed in y as "Those who know binary and those who don't"

print(f"I said: {x}") #String 1 - shows on the users screen what is typed in x formated with some extra text as  "I said : There are 10 Types of people.
print(f"I also said: '{y}'") #String 2 - shows on the users screen what is typed in y formated with some extra text as  "I also said: 'Those who know binary and those who don't'"

hilarious = False #set's the name "hilarious" as false, this is a boolean value
joke_evaluation = "Isn't that joke so funny?! {}" # set's the name and text for joke_evaluation

print(joke_evaluation.format(hilarious)) #String 3 combines joke_evaluation with the false of hilarious name

w = "This is the left side of..." # set's the data of the name w
e = "a string with a right side." # set's the data of the name e

print (w + e) #string 4 - combines W with e
