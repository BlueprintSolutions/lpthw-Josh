formatter = "{} {} {} {}"
formatter2 = "{} {} {}" # working out how formatter works

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format (
    "try your",
    "Own test here",
    "Maybe a poem",
    "Or a song about fear"
))
print(formatter.format(2,2,2,0)) #my test to understand what formatter is doing.
print(formatter2.format(1,2,3,0)) #interesting output is that formatter2 only outputs the first 2 variables in this string and not the rest.
print(formatter2.format("Josh", True, 1)) #seems you can add multiple variables in the formatter string.
