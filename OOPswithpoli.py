#class defination 
# A class is a blueprint of an house
#In simple terms (This is a desing to create calculator objects)
class Calculator:

   
# __init__ - costructor (special method )
# self - Reference to current object
# x,a,b - parameters (inputs ) 
# Run automatically when object is created 
# Initialization onject data
# simply it mean (when object is born ,store these values inside it )
    def __init__(self, x:int,a:int,b:int):
        # instance variables
        #  It store values inside the object
        # In other way (Put values into the object's memory)
        self.x = x
        self.a = a
        self.b = b


# Method - Function inside class
# self - Access current object 
# -> int - return integer 
    def calculate(self) -> int:
        return self.a * self.x**2 + self.b * self.x + 1  # perform calculation and send result back
                                                        # In other way (do the math and gove answer)

def main():   #Control function / Entry function or this controls the whole program 
    x = int(input("Enter the value of x: ")) #takes user input (string) and converts to number (same for a and b)
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))


    obj =  Calculator(x,a,b) # Object - instance of class  # constructor call
                        # object is created , __init__   runs and values stored inside objcet  
                        # Or we can say it create a calculator object with given values    
    result = obj.calculate() # Call method using object ,perform calculation  and store result 
                             # Tell object to calculate and give answer 
    print(f"Result: {result}") # Display result

if __name__ == "__main__":  # Entry point or Execution guard 
                         # Run only file is executed directly 
                         # In other terms it start program only  when user run this file
    main() #start the program 