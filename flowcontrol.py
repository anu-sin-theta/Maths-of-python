H = int(input("Enter the height of tank in meters\n"))
R = int(input("Enter the radius of tank in meters\n"))
P = int(input("And whats the power of your pump in per minute\n"))
vol = 3.14 * (R**2) * H
time = int(input("enter pump onn time in minutes\n"))
fill = vol // P
print("Tank will be filled in ", fill, "minutes/minute")
if time == fill:
    print("Tanki bhar gyi hai ")
elif:
    print("Abhi thodi der aur chalao")


