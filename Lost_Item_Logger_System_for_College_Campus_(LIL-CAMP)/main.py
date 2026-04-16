from system.lilcamp_system import LILCAMP

system = LILCAMP()

while True:
    print("\n1.Add\n2.View\n3.Search\n4.Report\n5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        system.add_item()
    elif ch == "2":
        system.view_items()
    elif ch == "3":
        system.search()
    elif ch == "4":
        system.report()
    elif ch == "5":
        break
    else:
        print("Invalid")