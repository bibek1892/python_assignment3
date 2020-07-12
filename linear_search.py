#e. Linear Search


def linear_search(items, find_item):
    for index in range(0,len(items)):
        if find_item == items[index]:
            return index

res = linear_search([1,3,4,6,5,8,9,2,7], 5)
print(res)