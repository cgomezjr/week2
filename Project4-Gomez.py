print("This program will calculate the sphere's diameter, circumference, surface area, and volume when given the radius.")
radius = float(input("Input the radius of the sphere: "))
pi = 3.14159
sph_dia = radius * 2
circum = 2 * pi * radius
sur_area = 4 * pi * radius ** 2
vol = 4 / 3 * pi * radius ** 3
print("Sphere's diameter: " + str(sph_dia))
print("Circumference: " + str(circum))
print("Surface Area: " + str(sur_area))
print("Volume: " + str(vol))