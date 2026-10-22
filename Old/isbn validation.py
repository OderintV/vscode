''' Write a program to accept the year of graduation from school as an integer value from the user. Using the binary search technique on the sorted array of integers given below, output the message "Record exists" if the value input is located in the list/array. If not, output the message "Record does not exist".
Sample Input:

n[0]	n[1]	n[2]	n[3]	n[4]	n[5]	n[6]	n[7]	n[8]	n[9]
1982	1987	1993	1996	1999	2003	2006	2007	2009	2010 '''

import sys
isbn = input("Enter 10-digit ISBN: ")

if len(isbn) != 10 or not isbn.isdigit():
    print("Illegal ISBN")
    sys.exit()
else:
    total = sum((i + 1) * int(isbn[i]) for i in range(10))
    if total % 11 == 0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
        sys.exit()
