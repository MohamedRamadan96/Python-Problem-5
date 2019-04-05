# Question 5 :  Given a list of ints, return True if first and last number of a list is same
def is_First_and_Last_Same(numberList):
    firstElement = numberList[0]
    lastElement  = numberList[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False

numList = [10,3,2,7,4,8,10]
print("The first and last number of a list is same")
print("result is",is_First_and_Last_Same(numList))


