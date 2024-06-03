print("*****AREA CALCULATOR******")
print("""press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle""")

choice = int(input("enter your choice number btw 1-4: "))

if choice == 1:
    side = int(input("enter the length of one side"))
    area = side**2
    print("area of square is: ", area)

elif choice == 2:
    length = float(input("enter the length of the rectangle: "))
    width = float(input("enter the width of the rectangle: "))
    area = length*width
    print("area of rectangle is: ", area)

elif choice == 3:
    radius = float(input("enter the radius of the circle: "))
    area = (22/7)*(radius**2)
    print("area of circle is: ", area)

elif choice == 4:
    base = float(input("enter the base of the triangle"))
    height = float(input("enter the height of the triangle"))
    area = 0.5*base*height
    print("area of the triangle is: ", area)

else:
    print("invalid input")