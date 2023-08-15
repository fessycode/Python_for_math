#!/usr/bin/python3

def main():
    try:
        radius = float(input("Enter the value of radius: "))
        if radius < 0:
            print(" The value of radius can not be negative")
        else:
            volume, surface_area = volume_area_sphere(radius)
            print(f"The volume of sphere of radius {radius} is {volume:.2f} and the surface area is {surface_area:.2f}")
    except ValueError:
        print("Invalid input: Please enter a valid number.")
if __name__ == "__main__":
    main()

