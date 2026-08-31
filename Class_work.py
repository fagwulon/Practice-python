length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

Area = length * breadth

Perimeter = (length + breadth) * 2

print(f'Your area is {Area}')
print(f'Your perimeter is {Perimeter}')


time = int(input("Enter the number of seconds: "))

hours = time // 3600
minutes = (time % 360) // 60
seconds = time % 60

print(f"Actual time: {hours} hours, {minutes} minutes, {seconds} seconds")

print("Agatha is good")