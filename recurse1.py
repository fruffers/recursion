# recursive sum: add 2 the amount of times given

def sum(adder,num):
    if adder == 0:
        return num
    return sum(adder-1,num+2)



print(sum(5,0))
