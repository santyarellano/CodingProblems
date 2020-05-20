from os import system, name
from colorama import Fore
from colorama import Style
import math

testSudo = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def printSudoku(s):
    for i in range(9):
        for j in range(9):
            print(s[i][j], end=" ")
            if (j+1) % 3 == 0:
                print(" ", end=" ")
        if (i+1) % 3 == 0:
            print("\n")
        else: print("")

def removeFromList(possibleNums, arr):
    res = []
    for n in possibleNums:
        if not n in arr:
            res.append(n)
    return res

def getColumn(s, pos):
    col = []
    for i in range(9):
        col.append(s[i][pos])
    return col

def identifyBlock(s, x, y):
    xPos = math.floor(x/3)*3
    yPos = math.floor(y/3)*3
    return [yPos, xPos]

def getBlock(s, x, y):
    b = identifyBlock(s, x, y)
    x = b[1]
    y = b[0]
    block = []
    for i in range(y,y+3):
        for j in range(x,x+3):
            block.append(s[i][j])
    return block

def solveByCellUnique(s):
    cp = s
    hasFound = True
    while hasFound:
        hasFound = False
        for i in range(9):
            for j in range(9):
                if cp[i][j] == 0:
                    possibleNums = [1,2,3,4,5,6,7,8,9]
                    #remove nums from row
                    possibleNums = removeFromList(possibleNums, cp[i])
                    #remove nums from column
                    col = getColumn(cp, j)
                    possibleNums = removeFromList(possibleNums, col)
                    #remove nums from block
                    block = getBlock(cp, j, i)
                    possibleNums = removeFromList(possibleNums, block)
                    if len(possibleNums) == 1:
                        cp[i][j] = possibleNums[0]
                        hasFound = True
    return cp

def solve(s):
    # attempt to solve by finding cells with only one possible value
    cp = solveByCellUnique(s)
    return cp

def test(testName, output, expected):
    print(f"{testName}..........", end=" ")
    if output == expected:
        print(f'{Fore.GREEN}SUCCESS!{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}FAIL! ({output}) {Style.RESET_ALL}')

def hasZeros(s):
    for row in s:
        if 0 in row:
            return True
    return False

def tdd():
    # REMOVE FROM LIST
    testList = [1,2,3,6,8]
    checkList = [1,6,7,9]
    test("Remove from list returns right res (1)", removeFromList(testList, checkList), [2,3,8])
    testList = [2,3,4,6,8,9]
    checkList = [1,6,7,8,9]
    test("Remove from list returns right res (2)", removeFromList(testList, checkList), [2,3,4])
    print("")

    # GETS RIGHT COLUMN
    rightCol = [7,9,0,6,0,2,0,1,8]
    test("Gets right column (1)", getColumn(testSudo, 4), rightCol)
    rightCol = [0,0,0,3,1,6,0,5,9]
    test("Gets right column (2)", getColumn(testSudo, 8), rightCol)
    print("")

    # IDENTIFY BLOCK
    test("Identifies block (1)", identifyBlock(testSudo, 1, 1), [0,0])
    test("Identifies block (2)", identifyBlock(testSudo, 3, 5), [3,3])
    print("")

    # GET BLOCK
    rightBlock = [5,3,0,6,0,0,0,9,8]
    test("Gets right block (1)", getBlock(testSudo, 1, 1), rightBlock)
    rightBlock = [0,6,0,8,0,3,0,2,0]
    test("Gets right block (2)", getBlock(testSudo, 3, 5), rightBlock)
    print("")

    # HAS 0'S
    test("Solution contains no 0's", hasZeros(solve(testSudo)), False)
    print("")

    # FINAL SOLUTION
    solution = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]
    test("Returns right solution", solve(testSudo), solution)
    print("")

#---------------------------------------- MAIN -----------------------------------------------------
printSudoku(testSudo)
input("Press any key to solve...")
clear()
tdd()
res = solve(testSudo)
printSudoku(res)