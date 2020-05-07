import math

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    if index == -1: return False
    return True

def isPossibleRoad(road, storages):
    # checks if a road connects one storage and one free city
    if (BinarySearch(storages, road[0])) == (BinarySearch(storages, road[1])):
        return False
    return True

def problem(n, m, k, roads, storages):
    if k == 0 or k == n:
        return -1
    
    # sorting approach
    storages.sort()
    roads.sort(key=lambda x: x[2])
    for r in roads:
        if isPossibleRoad(r, storages):
            return r[2]

    return -1


def asrtEq(testNum, v1, v2):
    print(f"Test {testNum}....... ", end="")
    if v1 == v2: 
        print(f"SUCCESS")
        return True
    else: 
        print(f"FAIL ({v1} != {v2})")
        return False

def tdd():
    # test 1
    n=5
    m=4
    k=2
    roads=[
        [1, 2, 5],
        [1, 2, 3],
        [2, 3, 4],
        [1, 4, 10]
    ]
    storages=[1, 5]
    res = problem(n, m, k, roads, storages)
    if not asrtEq(1, res, 3): return False

    # test 2
    n=3
    m=1
    k=1
    roads=[
        [1, 2, 3]
    ]
    storages=[3]
    res = problem(n, m, k, roads, storages)
    if not asrtEq(2, res, -1): return False

    # test 3
    n=6
    m=7
    k=4
    roads=[
        [5, 6, 21],
        [3, 6, 18],
        [1, 6, 5],
        [4, 6, 4],
        [1, 2, 13],
        [3, 4, 7],
        [1, 2, 15]
    ]
    storages=[6, 1, 3, 2]
    res = problem(n, m, k, roads, storages)
    if not asrtEq(3, res, 4): return False

def user():
    aux = list(map(int, input().split()))
    n=aux[0]
    m=aux[1]
    k=aux[2]
    roads = []
    for i in range(m):
        aux = list(map(int, input().split()))
        roads.append(aux)
    storages = []
    if k > 0: 
        storages = list(map(int, input().split()))
    res = problem(n, m, k, roads, storages)
    print(res)

#------------- MAIN ----------------
test = False
if test:
    tdd()
else:
    user()