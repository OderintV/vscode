# string to num

def num_to_zero(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n <10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n-10]
    elif 20 <= n <100:
        if n %10 == 0:
            return tens[n//10]
        else:
            return tens[n // 10] + "-" + ones[n % 10]
    else:
        return ("not in range ")

print(num_to_zero(99))

    