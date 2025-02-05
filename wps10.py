# CS1210: WPS10 [2 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
# 1) the code below is entirely your work, and
# 2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid" between the two double quote marks
# to match your own hawkid. Your hawkid is the "login identifier" you use
# to login to all University services, like `https://myUI.uiowa.edu/'
#
#
# Note: we are not asking for your password, just the login
# identifiers: for example, mine is "sriram".
#
# Replace the pass statement below by your code
######################################################################
def signed():
    return(["mharbaugh"])

######################################################################
# SPECIFICATION
# D is a (possibly empty) dictionary of variables and associated values, e.g., 
# D could be {"y": 3, "count": 0, "i": 1, "z": 10}. Thus, the keys of D are 
# strings and the values are integers. expression is a string representing an 
# arithmetic expression containing variables and the "+" operator. You can
# assume that each variable contains only upper or lower case characters. 
# For example, expression could be  "   y +z+z  +count ".
# The function should return the value of the expression obtained after 
# substituting values for the variables in the expression. For example,
# with D equal to {"y": 3, "count": 0, "i": 1, "z": 10} and expression
# equal to "   y +z+z  +count ", the function call evaluate(D, expression)
# should return 23 since 3 + 10 + 10 + 0 is 23.
# Note that the expression is a string with arbitrarily many spaces between
# consecutive items in the expression. The expression is guaranteed to 
# contain only the + operator and will be correctly formed (e.g., there 
# will not be two consecutive + operators or two consecutive variables not 
# separated by +). However, it is not guaranteed that the variables in 
# the expression are present in the given dictionary D. If this happens, 
# the function should just return {None} since it cannot evaluate 
# the expression.
# 
# EXAMPLES:
# evaluate({"test": 11, "count": -1}, "test + test + count") returns 21
# evaluate({"test": 11, "count": -1}, "x + test + test + count") returns None
# evaluate({"test": 11, "count": -1, "x": 25}, "x + test + test + count")
# returns 46
######################################################################
def evaluate(D, expression):
    x1 = []
    x2 = []
    i = 0
    x = expression.split("+")
    for each in x:
        x1.append(each.strip())

    while i < len(x1):
        if x1[i] in D:
            x2.append(x1[i].replace(x1[i], str(D[x1[i]])))
            x2[i] = int(x2[i])
            i = i + 1
        else:
            return None
    
    return sum(x2)
    
######################################################################
# This is the recursive binarySearch function we discussed in class. 
# This function only returns a boolean value. You are required to use
# this to write an "enhanced" binarySearch function called binarySearchPlus
# whose specification is described below.
######################################################################
def binarySearch(L, x, first, last):
    xSmall = []
    xLarge = []
    
    if x in L:
        return L.index(x)
    else:
        for each in L[first:last+1]:
            if x < each:
                xSmall.append("1")
                if len(xSmall) == len(L[first:last+1]):
                    return (first-1)
            else:
                for each in L[first:last+1]:
                    if each < x:
                        xLarge.append(each)
                return L.index(xLarge[-1])
    
    
######################################################################
# SPECIFICATION
# L is a list of distinct numbers in increasing order and x is an arbitrary 
# number. If x is among the elements L[first], L[first+1], ..., L[last], the 
# function returns the index of x in L. If x is not among these elements,
# the function returns the index of the largest element in L[first], 
# L[first+1], ..., L[last] that is less than x. If x is smaller than all
# elements in L[first], L[first+1], ..., L[last], the function returns first-1.
#
# YOU ARE REQUIRED TO MODIFY THE CODE FOR RECURSIVE BINARY SEARCH GIVEN ABOVE.
# 
# EXAMPLES:
# binarySearchPlus([2, 3, 4, 9], 11, 0, 3) returns 3
# binarySearchPlus([2, 3, 4, 9], 1, 0, 3) -1
# binarySearchPlus([2, 3, 4, 9], 2.5, 0, 3) returns 0
# binarySearchPlus([2, 3, 4, 9], 6, 0, 3) returns 2
# binarySearchPlus([2, 3, 4, 9], 6, 0, 1) returns 1
# binarySearchPlus([2, 3, 4, 9], 1, 2, 3) returns 1
######################################################################
def binarySearchPlus(L, x, first, last):
    f = binarySearch(L, x, first, last)
    return f





















