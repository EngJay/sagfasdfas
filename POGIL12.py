import math

def calculateArea(r):
    area = math.pi * r ** 2

def main():
    radius = int(input("Enter the radius: "))
    calculateArea(radius)
    print("Area of a circle with a radius of", format(area, ".2f"))


main()


            
