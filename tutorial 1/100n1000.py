for num in range(100, 1001):
    temp = num
    digit_sum = 0
    
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
        
    if digit_sum % 9 == 0:
        print(num, end=" ")