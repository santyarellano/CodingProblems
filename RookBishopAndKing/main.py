def main(inp):
    origin = [inp[0], inp[1]]
    destination = [inp[2], inp[3]]
    res = ""
    # lets go for rook
    #   check if already in place
    #   if not, check if 1 move is the solution
    #   if not, then it's 2 moves
    if origin == destination:
        res += "0 "
    elif origin[0] == destination[0] or origin[1] == destination[1]:
        res += "1 "
    else:
        res += "2 "
    # lets go for bishop
    #   check if already in place
    #   if not, check if available in 1 move
    #   if not, check if available in 2 moves
    #   if not, then it cannot be done
    if origin == destination:
        res += "0 "
    elif abs(origin[0] - destination[0]) == abs(origin[1] - destination[1]):
        res += "1 "
    elif 
    # lets go for king

    return res

def test(testNum, inp, ans):
    print("Case "+str(testNum)+"..........", end=" ")
    res = main(inp)
    assert res == ans, "out: "+ str(res)+" Should be: "+str(ans)
    print("Success!")

def tdd():
    test(1, [4, 3, 1, 6], "2 1 3")
    test(2, [5, 5, 5, 6], "1 0 1")

# execute test (only during development)
tdd()