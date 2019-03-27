from sys import argv #Imports the functions of argv package from python

script, filename = argv #set's the variables of argv in this case the script name and the filename (to be inputted by user later on).

txt = open(filename) #opens the filename you specific in the terminial in this case ex15_sample.txt

print(f"Here's your file {filename}:") #prints what is in the file that is selected.
print (txt.read()) #reads the information of file ex15_sample.txt and prints it in the terminial
print(txt.close()) #closes the file after reading it

print("Type the filename again:") #shows on the terminal the words "Type the filename again"
file_again = input("Enter file name here ") #creates an input for the users to type the file name again and uses a cursor of text, I replaceed the >

txt_again = open(file_again) #Assigned the value of opening any text file to the name txt_again

print(">>>> argv=", repr(argv)) #using this each exercise to see what the script is saying.
print(txt_again.read()) #displays the text from the file ex15_sample.txt in the terminal by reading it and printing the text.
print(txt_again.close()) #closes the file after reading it
