brands = {"Nike":{
          "tiger":15000,
          "whiteb":40000,
          "black": 1300
                        },
         "Bata": {
             "jagwar":8900,
             "cobra":6000,
             "mamba":5700  },
         "Adidas":{
             "jerk":8900,
             "sandal":6700,
             "meoo":5000
         }
             }
cart = []

def menu():
    print("========Welcome to the shope=======")
    print("1: view shoes")
    print("2:view cart")
    print("3: exit")

def brand():
    print("brand 1, NIke")
    print("brand 2, Bata")
    print("brand 2, Adidas")


while True:
    menu()
    choice = input("Enter a choice from 1,3:")
    if choice == "1":
        print(brand())
        choose = input("Choose a brand from 1,3:")
        if choose == "1":
            print(brands["Nike"])
            select = input("Select the pair of shoes you want(1,3):")
            if select == "1":
                cart.append(brands["Nike"(0)])
            elif select == "2":
                cart.append(brands["Nike"(1)])
            elif select == "3":
                cart.append(brands["Nike"(2)])
            
        elif choose == "2":
            print(brands["Bata"])
            select = input("Select the pair of shoes you want(1,3):")
            if select == "1":
                 cart.append(brands["Bata"(0)])
            elif select == "2":
                 cart.append(brands["Bata"(1)])
            elif select == "3":
                  cart.append(brands["Bata"(2)])
                        
        elif choose == "3":
            print(brands["Adidas"])
            select = input("Select the pair of shoes you want(1,3):")
            if select == "1":
                 cart.append(brands["Adidas"(0)])
            elif select == "2":
                cart.append(brands["Adidas"(1)])
            elif select == "3":
                cart.append(brands["Adidas"(2)])
                        
        else:
            print("invalid option choose from 1,3")
            


    elif choice == "2":
        print(f"your cart is {cart}")
    elif choice == "3":
        print("Thanks for using")
        break
    else:
        print("invlaid choice choose from 1,3")

print(cart)


    