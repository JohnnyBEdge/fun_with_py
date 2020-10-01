

def countCurses():
    with open("die_hard.txt") as input_file:
#     # "count should include any variation of curse words such as fucker and asshole"
        curses=['fuck','shit','damn','bitch','dammit',' ass','bastard']
#     # test="shit fuck fucker fuckhead ass damn bastard dammit"
        joined_lines = " ".join(line.strip() for line in input_file)
    # for line in input_file:


        for i in curses:
            for word in joined_lines.split(' '):
                occurances = joined_lines.count(i)
                
            print(f"{i}:{occurances}")

countCurses()