"I am 6'2\" tall." # escape double-quote inside string
'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
formatter = "{} {} {} {}"


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Cßatnip\n\t* grass
"""

fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Cßatnip\n\t* grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(fat_cat2)
print(formatter.format(1,2,3,4))
