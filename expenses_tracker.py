list = ["1:food","2:education","3:tech","4:exit"]
total = 0
spend = 0
print("________welcome________")

while True:
        print(f"choce one thing {list}")

        choice = int(input("Enter your choice:"))
        if choice > 5:
            print("choose number between 1 to 4")
        match choice:
            case 1:
              float = int(input("Enter the amount spend on food:"))
              if float <= 0 :
                print("Amount must be in positive:")
              else:
                spend = spend + float
                print(spend)
                continue
            case 2:
              float = int(input("Enter the amount spend on education:"))
              if float <= 0 :
                 print("Amount must be in positive:")
              else:
                  spend = spend + float
                  print(spend)
                  continue
            case 3:
                     float = int(input("Enter the amount spend on tech:"))
                     if float <= 0 :
                         print("Amount must be in positive:")
                     else:
                         spend = spend + float
                         print(spend)
                         continue
            case 4:
                print("Thnaks for using")
                break
result = spend + total
print("_______________________")
print(f"your total is {result}")
print("_______________________")

        
        



