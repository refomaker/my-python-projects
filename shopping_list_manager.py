items = ["milk", "eggs", "bread", "butter"]

while (True):
    print("===== SHOPPING LIST =====")
    print("1. show items")
    print("2. add item")
    print("3. remove item")
    print("4. exit")
    
    mode = input("what do you wanna see? 1/2/3/4:")

    if mode not in ("1", "2", "3", "4"):
        print("invalid mode bro..., please try again and add numbers")
        continue

    if mode =="4":
        break

    if mode =="1":
        print("===== SHOPPING LIST ITEMS =====")
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]}")
    elif mode == "2":
        items.append(input("enter the item you wanna add: "))
        print("item was added succsesfully !!")
    elif mode =="3":
        print("===== REMOVE ITEM =====")
        item = input("enter the item you wanna remove: ")
        if item in items:
            items.remove(item)
            print("item was removed succsesfully !!")
        else:
            print("item not found in the list, please try again")
        
    print("goodbyyee!!")