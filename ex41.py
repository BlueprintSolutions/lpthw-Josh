import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%% (object):\n\tdef__init__(self, ***)":
    "class %%% has-a__init__that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "English":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up thenwords fromn the website.
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                  random.sample(WORDS,snippet.count("%%%"))]
    other_names = random.sample(WORDS,snippet.count("***"))
    results = []
    param_names = []

    for i in range (0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:] #Python's way of copying a list. Using the list slice syntax [:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake paramert lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going unitl they hit CTRL-D
try:
        while True:
            snippets = list(PHRASES.keys())
            random.shuffle(snippets)

            for snippet in snippets:
                phrase = PHRASES[snippet]
                question, answer = convert(snippet, phrase)
                if PHRASE_FIRST:
                    question, answer = answer, question

                print(question)

                input("> ")
                print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")





print('-' * 10)
print("Word Drills")
print("""
class - Tells python to make a new kind of thing.
object - Two meanings: the most basic kind of thing, and any instance of something.
instance - What you get when you tell python to create a class (__int__)
def - How you define a function inside a class. (def)
self - inside the functions in a class, self is a variale for instance / object being accessed
inheritence - The concept that one class can inherit traits from another class, much like you and your parents.
composition - The concept that a clase can be composed of other classes as parts, much like how a car has wheels.
attribute - A property classes have that are from composition and are usually variables
is-a - A phrase to say that something inherits from another, as in a "salmon" is-a "fish".
has-a - A phrase to say that something is composed of other things or has a trait, as in "a salmon has a-mouth"
""")

print('-' * 10)
print("Python Code Snippet examples")
print("""
X: class X(Y): Make a class named X that is-a Y
Y: class X(object):def_init_(self,J): class x has-a__init__that takes self and J parameters.
M: class X(object):def M(self,J): class X has-a function named M that takes self and J parameters.
J: foo = x(): Set foo to an instance of class X.
K: foo.M(J): from foo get the M function, and call it with parameters self,J.
Q: foo.K = Q: from foo get K attribute, and set it to Q
""")

print('-' * 10)
print("Python Code Snippets Q&A")
print("""
1. make a class named ___ that is-a Y : X
2. class ___ has a__init__that takes self and ___ parameters" : Y
3. class ___ has-a function named ___ that takes self and ___ parameters : M
4. set foo to an instance of class ___ : J
5. from foo to get the ___ function, and call it with self=___ and parameters ___ : K
6. from foo get the ___ attribtue and set it to ___ : Q
""")
