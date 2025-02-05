
# CS1210: WPS4 [2 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your work, and
#  2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid" between the two double quote marks
# to match your own hawkid. Your hawkid is the "login identifier" you use 
# to login to all University services, like  `https://myUI.uiowa.edu/'
#
#
# Note: we are not asking for your password, just the login
# identifiers: for example, mine is "sriram".
#
######################################################################

def signed():
    return(["mharbaugh"]) 
    
######################################################################
# Complete this function
#
# Specification: The function takes a non-empty bitonic list L as 
# argument and returns the index of the maximum element in L.
#
# Examples: bitonicMax([2, 3, 11, 4]) returns 2
#           bitonicMax([2, 3, 14, 22, 30]) returns 4
#           bitonicMax([11, 20, 12, 9, 8, 2, 1]) returns 1
#           bitonicMax([30, 22, 12, 10, 4, 2, 1]) return 0
#           bitonicMax([4]) returns 0
#

######################################################################
def bitonicMax(L):
    first = 0
    last = len(L)-1
    mid = ((first + last) // 2)
    
    if len(L) > 0:
        print (mid)
        while first <= last:
            if L[mid] < L[mid + 1]:   #list is increasing
                first = mid + 1
            elif L[mid] > L[mid + 1]: #list is decreasing 
                last = mid - 1
            else:
                return L[mid]   
    
    pass


######################################################################
# Complete this function
#
# Specification: The function should return the number of points in L that are 
# contained in the axis-parallel rectangle R. For a point to be contained in R, 
# it appears somewhere in the interior or on the boundary of R.
#
# Examples: countPointsInRectangle([[0, 0], [4, 5]],  [[2, 3], [-1, -1], [2, 7], [0, 4]]) 
#           returns 2 
#
#           countPointsInRectangle([[1.5, 2], [4.0, 3.5]],
#                                  [[2.5, 5], [2, 3.5],[3.5, 1], [40, 2], [4.0, 3.1], [3.0, 2.25]]) 
#           returns 3.
#
#
# Replace the pass statement below by your code
######################################################################
def countPointsInRectangle(R, L):
   pass
    
    
    
    
    
    
    