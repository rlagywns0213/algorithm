hour, minute = map(int, input().split(" "))
how_many_times = int(input())

def hour_minute(hour,minute,how_many_times):
    if (minute + how_many_times) >= 60:
        minute = minute + how_many_times
        while minute > 59:
            minute = minute - 60
            hour = hour+1
    else:
        minute = minute + how_many_times
    if hour > 23:
        hour = hour - 24
    return hour, minute

hour, minute = hour_minute(hour, minute, how_many_times)
print(hour, minute)