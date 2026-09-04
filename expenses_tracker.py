list = ["1:food","2:education","3:tech"]
spend = []
print(f"choce one thing {list}")


choice = input("Enter your choice:")
match choice:
        case "1":
            float = int(input("Enter the amount spend on food"))
            if float < 0 :
                print("Amount must be in positive:")
            else:
                spend.append[float]
        case "2":
             float = int(input("Enter the amount spend on education:"))
             if float < 0 :
                 print("Amount must be in positive:")
             else:
                 spend . append[float]
        case "3":
                     float = int(input("Enter the amount spend on tech:"))
                     if float < 0 :
                         print("Amount must be in positive:")
                     else:
                         spend . append[float]
print(spend)
        
        



