cart = []

# Function to add item into the cart
def addItem():
    print("Keep entering items to your cart.\nEnter 's' to stop")
    while (True):
        item = input()
        if (item == 's'):
                break
        else:
            cart.append(item)

# Function to delete items from the cart
def deleteItem():
    print("Enter items to remove from cart>\nEnter 's' to stop")
    while (True):
        item = input()
        if (item == 's'):
            break
        elif(item not in cart):
            print("Item is not there in the cart. Enter another item")
        else:
            cart.remove(item)

# Function to display the items in the cart
def dispalyItems():
    length = len(cart)
    print("Items in your cart:")
    if (length == 0):
        print("Your cart is empty!")
    else:
        for i in range (0, length, 1):
            print(i+1,". ", cart[i])

# Main
print("WELCOME TO SUPERMART")
choice = 'y'
while (choice == 'y' or choice == 'Y'): # Customer can add, remove or display their cart as long as this condition is true
    print("Choose actions from the menu below:")
    print("1. Add Item\n2. Delete Item\n3. Display Items")
    ch = input("Enter choice: ") # Customer choses what to do

    if (ch == '1'):
        addItem()

    elif (ch == '2'):
        deleteItem()

    elif (ch == '3'):
        dispalyItems()

    else:
        print("Enter a valid choice!!")

    choice = input("Do you want to continue?\nEnter 'y' to continue or 'n' to quit: ")