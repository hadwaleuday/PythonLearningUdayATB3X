def sum_digits(num):
    sum_digit = 0
    while num > 0:
        sum_digit = sum_digit + (num%10)
        num = num // 10
        # /  - div
        # // Quotient
        # % - Reminder

    return sum_digit


print(sum_digits(123))
