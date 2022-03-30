a, b = map(int, input().split(' '))
if (b>45) & (a>0):
    hour_result = a
    min_result = b-45
elif a ==0:
    hour_result = 23
    if b<45:
        min_result = 60 - abs((b-45))
    elif b == 60:
        hour_result = 24
        min_result = 0
    else:
        hour_result =0
        min_result = b - 45
        
else:
    hour_result = a-1
    min_result = 60 - abs((b-45))
    if min_result == 60:
        hour_result = a
        min_result = 0
print(f'{hour_result} {min_result}')    