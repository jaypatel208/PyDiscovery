shopping_list = []
item_added = 0


def shopping_list_manager(item):
    shopping_list.append(item)


while item_added < 4:
    item = input("What item do you want to add: ")
    shopping_list_manager(item)
    item_added += 1


print("Current shopping list:", sorted(shopping_list))


shopping_list.pop()
print("Updated shopping list (last item removed):", shopping_list)
