def simple_calculator():
    
    status = False
    while status == False:
        
        try:
            finalnum = ""
            
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            op = input("Enter the operation: ")

            list = ["addition","substraction","multiplication","division"]

            if op  == list[0]:
                finalnum = num1 + num2

            elif op == list[1]:
                finalnum = num1 - num2

            elif op == list[2]:
                finalnum = num1 * num2

            elif op == list[3]:
                finalnum = num1/num2
                
            else:
                print("You have entered a wrong operation, try again.")
                continue
                    

        except ValueError:
            print("Enter a valid number")
            continue
            

        except ZeroDivisionError:
            print("Number cannot be divided by zero")
            continue
        
        except:
            print("Your input gives errors, try again")
            continue
        
        else:
            return finalnum
        
        
print(simple_calculator())