destination = input("please enter your destination: ")
distance = float(input("enter the distance in the kilometers; "))
speed = float(input("enter the speed in km/hr"))

hour = int(distance / speed)
module = distance % speed
minute = (module * 60) / speed

print(f"Destination: {destination}")
print(f"Distance: {distance}")
print(f"average speed: {speed}")

print(f"ETA: {hour}hrs {round(minute, 1)}min")