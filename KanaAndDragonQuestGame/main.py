import math

def weakDragon(health, voids, lighting):
    min2Kill = lighting * 10
    if min2Kill == 0: return False
    if health <= min2Kill: return True
    for x in range(voids):
        health = math.floor(health/2) + 10
        if health <= min2Kill: return True
    return False

def main(t, cases):
    for dragon in cases:
        if weakDragon(dragon[0], dragon[1], dragon[2]): print("YES")
        else: print("NO")

def tdd():
    t = 7
    cases = [
        [100, 3, 4],
        [189, 3, 4],
        [64, 2, 3],
        [63, 2, 3],
        [30, 27, 7],
        [10, 9, 1],
        [69117, 21, 2]
    ]
    main(t, cases)

def user():
    t = int(input())
    cases = []
    for x in range(t):
        inp=list(map(int, input().split()))
        cases.append(inp)
    main(t, cases)    

#----------------- MAIN -------------------------
testing = False
if testing: tdd()
else: user()