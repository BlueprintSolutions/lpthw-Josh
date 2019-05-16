print("""
Check here: https://www.programiz.com/python-programming/keyword-list#as

Keywords:
    and      : will result into True only if both the operands are True.
    del      : Used to delete the reference to an object. You can delete a variable reference using del.
    from     : Used to import modules into the current namespace e.g. import math
    not      : used to invert the truth value
    while    : used for looping in Python until a False or break statement is encounted.
    as       : used to create an alias while importing a module. Allows you to give a different name (user-defined) to a module while importing it.
    elif     : else if (used for conditional brannching and decision making)
    global   : used to declare that a variable inside the fucntion is global (Outside the function)
    or       : will result into True if any of the operands is true.
    with     : Used to wrap the execution of a block of code within methods defined by the context manager.
    asset    :
    assert   : (for debugging) if condition is true nothig happens, but if false AssertionError is raised.
    else     : When wanting to test some condition and exeute a block only if the condition is true we use if, and elif. elid is short for else if. else is the block which is executed if the condition is false.
    if       : Used for conditional execution e.g. if this than that.
    pass     : Is a null statement in python. Nothing happens, it's just used as a placeholder
    yield    : Used inside a function like a return statement. But yield returns a generator (iterator that generate one item at a time, instead of storing all value in memory like a list.)
    break    : Break is used inside for and while loops to alter the their normal behaviour. Break will end the smallest loop it is in and controls flows to the statement immediatly below the loop.
    except   : Exceptions are basically eroors that suggest something went wrong while executing the program. e.g. IOerror, ValueError, ZeroDivisionError, ImportError, NameError, TypeError, etc.. You can raise an exception explicitly with the raise keyword.
    import   : This keyword is used to import modules into the current document (Namespace) is used to import specific attributes or functions.
    print    : This function prints whatever is defined within the brackets () on the screen.
    class    : used to define a new user-defined class in Python
    exec     :
    in       : Used to test if a sequence (list, tuple, string, etc..) contains a value. It returns True if the value is present, else it returns False
    raise    : Is used to raise an error exception
    continue : Continue is used inside for and while loops to alter their normal behaviour. Continue causes the end the current interation of the lopp but not the whole loop.
    finally  : Finally is used with try_except block to close up resources or file streams. It ensures that the block of code inside it gets executed even if there is an unhandled exception.
    is       : Used in python for testing object identity. is, is used to test if the two varibales refer to the same object.
    return   : Is used inside a function to exit it and return a value.
    def      : Used to define a user-defined function
    for      : Used for looping. Generally is used when you know the number of times you want to loop somthing.
    lambda   : Used to create an anonymous function (function with no name). it's an inline function that does not contain a return statement. It consists of an experession that is evaluated and returned.
    try      : (used with exceptions in Python)

""")

print("""
Data Types:
    True    : Truth values in python, always the result of comparison operators or logical (Boolean) operations in Pyhton.
    False   : Fruth values in python, always the result of comparison operators or logical (Boolean) operations in Pyhton.
    none    : A constant in python that represents the absence of a value or a null value.
    strings : A sequence of Unicode characters. Can be represented using single, double or triple quotes.  e.g. ''This is a string''
    numbers : integers, floating point numbers, and complex numbers all fall under the python number category. They are defined as int, float, and complex class in Python.
    floats  :
    lists   : Is an ordered sequence of items. All the items in a list do not need to be of the same type. A list is declared by using enclosed brakcets [ ]

""")

print("""
String Escape Sequences:
Research: https://www.programiz.com/python-programming/string
If using quotes inside a string then you need an escape sequence to use the quote without breaking the string. e.g. print('''he said, what\'s there?''')
    \newline : backslash and newline ignored
    //       : backslash
    \'       : single quote
    \"       : double quote
    \a       : ASCII bell
    \b       : ASCII Backspace
    \f       : ASCII Formfeed
    \n       : ASCII Linefeed
    \r       : ASCII Carrage return
    \t       : ASCII Horizontal Tab
    \v       : ASCII Vertical Tab

""")

print("""
String Formats:
Research: https://www.programiz.com/python-programming/methods/string/format
https://realpython.com/python-string-formatting
    %d  : integers
    %i  :
    %o  :
    %u  :
    %x  :
    %e  :
    %E  :
    %f  : floating point numbers
    %F  :
    %g  :
    %G  :
    %c  :
    %r  :
    %s  : String (or any object with a string representatio, like numbers)
    %%  :

""")

print("""
Operators:
Research: https://www.programiz.com/python-programming/operators
https://data-flair.training/blogs/python-operator/
    +   : sum of e.g. x + Y
    -   : difference between e.g. x - y
    *   : product of e.g. x and y
    **  : to the power of
    /   : quotient of variables
    //  : floored quotient of variables
    %   : remainder of two numbers divided by one another
    <   : strictly less than
    >   : strictly more than
    <=  : Equal to or less than
    >=  : equal to or greater than
    ==  : equal
    !=  : not equal
    <>  : Does the same job as != but has been abandoned in Python 3
    ( ) :
    [ ] :
    { } :
    @   :
    ,   :
    :   :
    .   :
    =   : Assignment operator that assigned the value after the = to whatever variable is set on the right e.g. a = 5
    ;   :
    +=  : It adds right operand to the left operand and assign the result to left operand e.g. x += 5  is X = X + 5
    -=  : It subtracts right operand from the left operand and assign the result to left operand e.g. x -= 5  is X = X - 5
    *=  : It multiplies right operand with the left operand and assign the result to left operand e.g. x *= 5  is X = X * 5
    /=  : It divides left operand with the right operand and assign the result to left operand e.g. x /= 5  is X = X / 5
    //= : A compound operator that floor divides the variable and later assigns the same. e.g. x //= 5  is X = X // 5
    %=  : It takes modulus (remainder of a division on left operand by the right) using two operands and assign the result to left operand. e.g. x %= 5  is X = X % 5
    **= : It performs floor division on operators and assign value to the left operand. e.g. x **= 5  is X = X ** 5

""")
