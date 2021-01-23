# recursive add sum of numbers in a number

def sum(orig,num):
    if orig == 0:
        return num
    return sum(orig-1,num+orig)

print(sum(5,0))
