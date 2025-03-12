seconds_in = int(input("Enter time in seconds: "))

hours = seconds_in // 3600
remaining = seconds_in % 3600
minutes = remaining // 60
seconds = remaining % 60

formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
print(formatted_time)