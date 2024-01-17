print('# '*30, end="\n\n")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print('# '*30, end="\n\n")
if mins < 10:
    print(f"Die Startzeit des Events beträgt: {hour}:0{mins} Uhr")
else:   
    print(f"Die Startzeit des Events beträgt: {hour}:{mins} Uhr")

mins = mins + dura
duration_in_hours = mins / 60

hour = hour + int(duration_in_hours)

if mins >= 60:
    if hour >= 24:
        hour = hour % 24
    if mins >= 60:
        mins = mins % 60

if mins < 10:
    print(f"Die Endzeit des Events beträgt: {hour}:0{mins} Uhr")
else:
    print(f"Die Endzeit des Events beträgt: {hour}:{mins} Uhr")