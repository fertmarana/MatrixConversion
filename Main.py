import csv
import sys
def main():
    """testing"""
radius = float( input('Enter the radius of the circumference: ') )
coordinatex = float( input('Enter the coordinate x of the circumference: ') )
coordinatey = float( input('Enter the coordinate y of the circumference: ') )



choice = 4;
while (choice > 3 or choice < 1):
    """testing2"""
    choice = int (input('Which conversion method you want to use? (Insert Number)\n1 - Point Conversion\n2 - Polar Coordinate\n3 - Implicit Equation\n'))
    print ('choice value is', choice)
    if(choice < 4 and choice > 0):
        break

if (choice == 1):
    """Point Conversion"""
elif (choice == 2):
    """ Polar Coordinates """
elif (choice == 3):
    """Implicit Equation"""




#return