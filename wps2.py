#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CS1210: WPS2 [2 functions to complete]
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
# The argument m can be any non-negative integer
# Examples: numberOfDays(0) should be 0, numberOfDays(1) should be 31,
# numberOfDays(2) should be 59. For any m 12 or more, numberOfDays(m) should
# be 365.
#
######################################################################
def numberOfDays(m):
    if m == 0:
        return 0
    
    elif m == 1:
        return 31
    
    elif m == 2:
        return 59
    
    elif m == 3: 
        return 90
    
    elif m == 4:
        return 120
    
    elif m == 5:
        return 151
    
    elif m == 6:
        return 181
    
    elif m == 7:
        return 212
    
    elif m == 8:
        return 243
    
    elif m == 9:
        return 273
    
    elif m == 10:
        return 304
    
    elif m == 11:
        return 334
    
    elif m >= 12:
        return 365
        
    pass
    
######################################################################
# Complete this function
#
# The arguments month and day can be any positive integers. 
# Examples: weekDay(1, 28) should be "Saturday" , weekDay(2, 3) should be 
# "Friday".
# weekDay(2, 30), weekDay(20, 5), and weekDay (10, 200) should all be "".
#
######################################################################
def weekDay(month, day):
    num = numberOfDays(month-1) + day
    if month > 12:
        return ""
    
    if day > 31:
        return ""
    
    if (month == 2) & (day > 28):
        return ""
    
    if (month == 4) & (day > 30):
        return ""
    elif (month == 6) & (day > 30):
        return ""
    elif (month == 9) & (day > 30):
        return ""
    elif (month == 11) & (day > 30):
        return ""
    
    
    if num % 7 == 1:
        return "Sunday"
    
    elif num % 7 == 2:
        return "Monday"
    
    elif num % 7 == 3:
        return "Tuesday"
    
    elif num % 7 == 4:
        return "Wednesday"
    
    elif num % 7 == 5:
        return "Thursday"
    
    elif num % 7 == 6:
        return "Friday"
    
    elif num % 7 == 0:
        return "Saturday"
    
    pass



    