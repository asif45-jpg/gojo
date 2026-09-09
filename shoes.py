brands = {
    "Nike": {
        "tiger": 15000,
        "whiteb": 40000,
        "black": 1300
    },
    "Bata": {
        "jagwar": 8900,
        "cobra": 6000,
        "mamba": 5700
    },
    "Adidas": {
        "jerk": 8900,
        "sandal": 6700,
        "meoo": 5000
    }
}

# Keep consistent order for numbered menus (dicts preserve insertion order in 3.7+, but be explicit)
BRAND_ORDER = ["Nike", "Bata", "Adidas"]

cart = []


def ask(prompt):
    """input() that returns None on Ctrl-D / Ctrl-C instead of raising."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None


def menu():
    print("\n======== Welcome to the shop ========")
    print("1: view shoes")
    print("2: view cart")
    print("3: exit")


def show_brands():
    print("\nAvailable brands:")
    for i, name in enumerate(BRAND_ORDER, start=1):
        print(f"  {i}: {name}")


def show_models(brand_name):
    models = list(brands[brand_name].items())
    print(f"\n{brand_name} collection:")
    for i, (model, price) in enumerate(models, start=1):
        print(f"  {i}: {model:<10} Rs {price:,}")
    return models


def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return
    print("\nYour cart:")
    total = 0
    for idx, (brand_name, model, price) in enumerate(cart, start=1):
        print(f"  {idx}. {brand_name} - {model:<10} Rs {price:,}")
        total += price
    print(f"  {'TOTAL':<18} Rs {total:,}")


def shoe_shop():
    while True:
        menu()
        choice = ask("Enter a choice from 1-3: ")
        if choice is None:
            print("Thanks for using")
            break

        if choice == "1":
            show_brands()
            choose = ask("Choose a brand from 1-3: ")
            if choose is None:
                print("Thanks for using")
                break
            if choose not in ("1", "2", "3"):
                print("Invalid option — choose from 1-3.")
                continue

            brand_name = BRAND_ORDER[int(choose) - 1]
            models = show_models(brand_name)

            select = ask("Select the pair of shoes you want (1-3): ")
            if select is None:
                print("Thanks for using")
                break
            if select not in ("1", "2", "3"):
                print("Invalid selection — choose from 1-3.")
                continue

            model, price = models[int(select) - 1]
            cart.append((brand_name, model, price))
            print(f"Added to cart: {brand_name} - {model} for Rs {price:,}")

        elif choice == "2":
            view_cart()

        elif choice == "3":
            print("Thanks for using")
            break

        else:
            print("Invalid choice — choose from 1-3.")

    # show final cart on exit
    if cart:
        view_cart()
    else:
        print(f"Final cart: {cart}")


if __name__ == "__main__":
    shoe_shop()
