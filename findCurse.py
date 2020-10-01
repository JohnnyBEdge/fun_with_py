import re

def findCurse(curse):
    with open("die_hard.txt") as input_file:
        joined_lines = " ".join(line.strip() for line in input_file)
        split_lines = re.split('\.|\!|\?', joined_lines)
        count = 0
        for i in split_lines:
            if curse in i:
                count +=1
                print ( i.strip())
        print (f"There are {count} {curse}/s")

findCurse(" ass")