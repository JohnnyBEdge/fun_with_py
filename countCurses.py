

# with open("die_hard.txt") as input_file:

def countCurses():
    # "count should include any variation of curse words such as fucker and asshole"
    curses=['fuck','shit','damn','bitch','dammit', 'ass','bastard']
    test="shit fuck fucker fuckhead ass damn bastard dammit"
    # for line in input_file:
    for i in curses:
        occurances = test.split(' ').count(i)
        print(f"{i}:{occurances}")

countCurses()