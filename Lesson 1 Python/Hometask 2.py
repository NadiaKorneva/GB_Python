time_sec = int(input('Введите время в секундах:'))

hours = time_sec // 3600
minutes = (time_sec % 3600) // 60
seconds = (time_sec % 3600) % 60

# hours, minutes, seconds = user_seconds // 3600, (user_seconds % 3600) // 60, (user_seconds % 3600) % 60

print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
