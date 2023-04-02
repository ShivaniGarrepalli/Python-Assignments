def sum_of_squares(n):
    sum=0
    for i in n:
        sum += i*i
    return sum
n = [1, 2, 3, 4, 5]
result = sum_of_squares(n)
print(result) 

