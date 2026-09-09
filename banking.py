list = ["1:food","2:education","3:tech"]
CATEGORIES = {
    "1": ("food", 1500.0),
    "2": ("education", 1000.0),
    "3": ("tech", 2000.0),
}

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
        
        
budget_left = {key: budget for key, (_, budget) in CATEGORIES.items()}

QUIT = ("q", "quit", "exit")


def ask(prompt):
    """input() that returns None on Ctrl-D / Ctrl-C instead of raising."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None


def show_menu():
    print("\nYour categories:")
    for key, (name, budget) in CATEGORIES.items():
        print(f"  {key}: {name:<10} budget {budget:.2f}")


def choose_category():
    """Return (action, key): ('quit', None) or ('ok', '1') or ('again', None)."""
    choice = ask("Enter your choice (or 'q' to quit): ")
    if choice is None or choice.lower() in QUIT:
        return "quit", None
    if choice not in CATEGORIES:
        print(f"Unrecognized category: {choice!r}. Pick 1-3 or q to quit.")
        return "again", None
    return "ok", choice


def ask_amount(name):
    """Return (action, amount): ('ok', 500.0) or ('again'/'quit', None)."""
    raw = ask(f"Enter the amount spent on {name}: ")
    if raw is None:
        return "quit", None
    try:
        amount = float(raw)
    except ValueError:
        print("Amount must be a number.")
        return "again", None
    if amount <= 0:
        print("Amount must be positive.")
        return "again", None
    return "ok", amount


def record_expense(key, amount):
    name, budget = CATEGORIES[key]
    if amount > budget_left[key]:
        print(f"Over budget: {name} has only {budget_left[key]:.2f} left.")
        return
    budget_left[key] -= amount
    spend.append((name, amount))
    print(f"Logged {amount:.2f} on {name}. Remaining {name} budget: {budget_left[key]:.2f}")


def show_summary():
    total = sum(amount for _, amount in spend)
    print("\nExpenses:")
    for name, amount in spend:
        print(f"  {name:<10} {amount:>10.2f}")
    print(f"  {'TOTAL':<10} {total:>10.2f}")
    print("\nBudget left:")
    for key, (name, budget) in CATEGORIES.items():
        print(f"  {name:<10} {budget_left[key]:>10.2f} / {budget:.2f}")


def expenses_tracker():
    while True:
        show_menu()
        action, key = choose_category()
        if action == "quit":
            break
        if action == "again":
            continue
        action, amount = ask_amount(CATEGORIES[key][0])
        if action == "quit":
            break
        if action == "ok":
            record_expense(key, amount)
    show_summary()


if __name__ == "__main__":
    expenses_tracker()