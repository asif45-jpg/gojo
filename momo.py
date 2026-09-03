def banking_system():
    balance = 1000.0

    while True:
        print("1: check balance.")
        print("2: deposit amount.")
        print("3: withdrawl amount.")
        print("1: exit.")

        choice = input("Enter your choice from 1 to 4")
        match choice:
            case "1":
                print(f"your balnce is {balance}")
            case "2":
                amount = float(input("Enter deposit amount:"))
                if amount <= 0:
                    print("amount must be positive")
                else:
                    balance += amount
                    print(f"deposited {amount:.2f} . new Balance: {balance:.2f}")
            case "3":
                amount = float(input("Enter withdrawl amount:"))
                if amount <= 0:
                    print("amount must be positive")
                elif amount > balance:
                    print("print insufficient balnce:")
                else:
                    balance -= amount
                    print(f"withdrawl {amount:.2f}. new balance{balance:.2f}")
            case "4":
                print("thank you for using our bank system:")
                break
            case _:
                print("invalid activity:")
banking_system()