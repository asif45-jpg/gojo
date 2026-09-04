def gojo_grade():
    total = 500
    choicr = input("Enter what do you want:(1 or 2)")
    match choicr:
        case "1":
            while True:
                 math = int(input("Enter your maths number:"))
                 english = int(input("Enter your english number:"))
                 physics = int(input("Enter your physics number:"))
                 urdu = int(input("Enter your urdu number:"))
                 computer = int(input("Enter your computer number:"))
                 combine = math + english + urdu + computer + physics
                 
                 if combine >= 470:
                     print(f"your A grade ur total are{combine}")
                     break
                 elif combine >= 400:
                     print(f"your B grade ur total are{combine}")
                     break
                     
                 elif combine >= 370:
                     print(f"your c grade ur total are{combine}")
                     break
                 else:
                     print(f"ur fail ur combine are less than{combine}")
                     break
        case "2":
            print("thanks ") 
gojo_grade()
                   

            


            



