from sys import argv   #Imports the functions of argv package from python
from os.path import exists #Imports the functons of the os.path from python (Checks if a file or directory exists or not)

script, from_file, to_file = argv #set's the variables of argv

print(f"copying from {from_file} to {to_file}") #shows on the users screen what file we are copying from and to which file.

# we could do these two on one line too, how?
in_file = open(from_file); indata = in_file.read() #this is opening the file and reading it then placing that read file under the variable indata

#in_file = open(from_file)
#indata = in_file.read()

print(f"The input file is {len(indata)} long") #shows the user the length of the input file

print(f"Does the output file exist? {exists(to_file)}") #The exist function sees if the file actually exists
print("Ready, hit RETURN to continue, CTRL-C to abort.") #Shows the text inside the brackets on screen.
input("?") #allows the user to input information

out_file = open(to_file, 'w') #opens the files specificed in the argv to open so we can write to it
out_file.write(indata) #tells python to take the data we sorted in "indata" and write that to the out_file

print("Alright, all done.") #Shows the text inside the brackets on screen.

out_file.close() #closes the out_file
in_file.close() #closes the in_file

print("""
Opening the new file that you just created.
Would you like to add some text to it? Yes or No?
""") #Shows the text inside the brackets on screen.
out_file2 = open(to_file, 'w') #opens the out_file into a new variable called out-file2
want_to_edit = input("yes or no: ") #asks the user for an input of yes or no and stores that in the variable want_to_edit

if want_to_edit == ("no"): #if want_to_edit is no then it runs the print and close string below
    print("Well then I guess we can skip to closing the document")
    out_file2.close()
    print("The Document is now closed! Good day sir")

elif want_to_edit == ("yes"): #if want_to_edit is yes then runs the function below.
    print("truncating the file. :)") #Shows the text inside the brackets on screen.
    out_file2.truncate() #goes to the start of the document and completley wipes the document.

    print("Let's add some text to this document.") #Shows the text inside the brackets on screen.

    line1 = input("line 1: ") #asks the user to input data for line 1
    line2 = input("line 2: ") #asks the user to input data for line 2
    line3 = input("line 3: ") #asks the user to input date for line 3

    print("Let's write these lines to the file using 1 line of code")

    out_file2.write(line1 + "\n" + line2 + "\n" + line3 + "\n") #writes the contents written on each file to the out_file2
    print("and now we close the document") #Shows the text inside the brackets on screen.
    out_file2.close()  #closes the out_file2

    print(">>>> argv=", repr(argv))

    print("Let's open the file and read it again") #Shows the text inside the brackets on screen.
    out_file3 = open(to_file, 'r') #opens to_file to read and sets it as the variable out_file3

    print(out_file3.read()) #prints on the screen the contents of out_file3

    print("Don't forget to close the document again") #Shows the text inside the brackets on screen.
    out_file3.close()

    print("Aren't you just a good boy!") #Shows the text inside the brackets on screen.

while want_to_edit not in ("yes","no"): #looks to see if yes or no have been entered if not then it runs the print screen function on the next line
    print("You did'nt select a valid option and now I am going to have a melt down ARGGGGGHHHH") #Shows the text inside the brackets on screen.
    break
