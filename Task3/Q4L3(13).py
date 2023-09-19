class currency_converter:
    
        def __init__(self):
            while True:
                print('''
            welcome ... choose 1 of Currencies to Convert from EGP to:
              1:USD - 2:KWD - 3:GBP - 4:CAD - 5:BHD - 6:CHF - 7:EUR
                ''')
                User_choise = int(input("Enter your Currency :"))
                if User_choise in range(1,8):
                    amount = float(input("Enter your Amount :"))
                    if User_choise == 1:
                        currency = (0.032*amount)
                        print(f'{currency} USD')
                        
                    elif User_choise == 2:
                        currency = (0.0100*amount)
                        print(f'{currency} KWD')

                    elif User_choise == 3:
                        currency = (0.026*amount)
                        print(f'{currency} GBP')

                    elif User_choise == 4:
                        currency = (0.044*amount)
                        print(f'{currency} CAD')
                       
                    elif User_choise == 5:
                        currency = (0.012*amount)
                        print(f'{currency} BHD')
                     
                    elif User_choise == 6:
                        currency = (0.029*amount)
                        print(f'{currency} CHF')
                    
                    elif User_choise == 7:
                        currency = (0.030*amount)
                        print(f'{currency} EUR')
                        
                else:
                    print ("Please Enter Numbers between 1:7 or Exit")

                play_again = input("Press any key to check again , Q to Exit")
                if play_again == "Q":
                        print("Goodbye ...")
                        break
  
c1 = currency_converter()
