def main() :
    num = check('Enter an integer to check whether its a prime number or not : ')
    checked = num
    if checked == True :
        print('The number is a prime')
    elif checked == False :
        print('The number is not a prime')
        
def check(prompt) :
    while True :
        num = input(prompt)
        try :
            num = int(num)
            prime = True
        
            if num == 0 or num == 1 :
                prime = False
            elif num >= 2 :
                for i in range (2, num) :
                    if num % i == 0 :
                        prime = False
                        break
                    else:
                        prime = True
            return prime
        except :
            print('Invalid entry')
main()
                    
                    
                

            
