''' A special two-digit number is such that when the sum of its digits is added to the product of its digits, the result is equal to the original two-digit number.

Example: Consider the number 59.
Sum of digits = 5 + 9 = 14
Product of digits = 5 * 9 = 45
Sum of the sum of digits and product of digits = 14 + 45 = 59

Write a program to accept a two-digit number. Add the sum of its digits to the product of its digits. If the value is equal to the number input, then display the message "Special two—digit number" otherwise, display the message "Not a special two-digit number". '''

n = int(input("enter num: "))

print ("special two digit no" if (int(str(n)[0]) + int(str(n)[-1]) + int(str(n)[0]) * int(str(n)[-1])) == n else "not a special two digit no")
