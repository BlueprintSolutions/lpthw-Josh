print("""

1. True and True : True
2. False and True : False
3. 1 == 1 and 2 ==1 : False
4. test == test : True
5. 1 == 1 or 2 != 1 : True
6. True and 1 == 1 : True
7. False and 0 != 0 : False
8. True or 1 == 1 : True
9. "test" == "testing" : False
10. 1 != 0 and 2 == 1 : True
11. "test" != "testing" : False
12. "test" = 1  ; False
13. not (True and False) : True
14. not (1 == 1 and 0 != 1) : False
    not (True and True)

15. not (10 == 1 or 3 == 4) : True
    not (False or False)

16. not (1 != 10 or 3 == 4) : False
    not (True or False)

17. not ("testing" == "testing" and "Zed" == "Cool Guy") : True
    not (True and False)

18. 1 == 1 and not ("testing == 1 or 1 == 0") : True
    True and not (False or False)
    True and True

19. "chunky" == "bacon" and not (3 == 4 or 3 == 3) :  False
    False and not (False and True)
    False and False

20. 3 == 3 and not ("testing" == "testing or "Python" == "Fun") : False
    True and not (True or False)
    True and not (False)

21. 3 != 4 and not ("testing" != "test" or "Python" == "Python") : True
    3 != 4 is True: True and not ("Testing" != "test" or "Python" == "Python")
    "testing" != "test" is True: True and not (True or "Python" == "Python")
    "Python" == "Python": True and not (True or True)
    True and not (True or True)
    True and True

""")
