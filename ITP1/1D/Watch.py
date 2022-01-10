input_second = int(input())

second = input_second % 60
minute = int(input_second / 60) % 60
hour = int(input_second / 3600)

print(hour, minute, second, sep=':')
