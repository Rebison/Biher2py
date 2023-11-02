def main():
    print("Enter the Name of File: ") 
    fileName = "abc.txt"
    try:
        fileHandle = open(fileName, "r") 
        tot1 = 0
        tot2 = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for char in fileHandle.read():
            if char in vowels: 
                tot1 = tot1+1
            if char>='a' and char<='z':
                if char not in vowels:
                    tot2 = tot2+1
            elif char>='A' and char<='Z':
                if char not in vowels:
                    tot2 = tot2+1 
        fileHandle.close()
        print("The number of Vowels is: %d\nThe number of consonants is: %d"%(tot1,tot2)) 
    except IOError:
        print("\nError Occurred!")
        print("Either File doesn't Exist or Permission is not Allowed!")


if __name__ == '__main__':
    main()
