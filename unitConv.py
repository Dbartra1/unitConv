##Functions##
def titlePrint():
    print ('\nFeet and Meters Converter\n')
def menuPrint():
    print ('Conversions Menu: ' +
           '\na. Feet in Meters' +
           '\nb. Meters to Feet')
def feetMeters(x):
        f = x * 0.3048
        print (round(f, 2), ' meters\n')
def metersFeet(y):
        m = y / 0.3048
        print (round(m, 2), ' Feet\n')

def main():
    titlePrint()
    menuPrint()
    choice1 = 'y'
    while choice1.lower() == 'y':
        while True:
            choice2 = input("\nWhat Conversion Would You Like To Make? (a/b): ")
            if choice2.lower() == 'a':
                x = float(input("\nHow many feet?: "))
                print()
                feetMeters(x)
                break
            if choice2.lower() == 'b':
                y = float(input("\nHow many Meters?: "))
                print()
                metersFeet(y)   
                break
            else:
                print ("\nPlease Make a Proper Selection")
                continue
        choice1 = str(input("Would you like to continue? (y/n): "))
        if choice1.lower() != 'y':
            print("\nBYE!!!!")
            break

    
            
        
if __name__ == "__main__":
    main()
    


    

