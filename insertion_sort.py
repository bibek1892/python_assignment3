# b) Insertion Sort

def insertion_sort(items):
    len_of_list = len(items)
    for i in range(0,len_of_list):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j+1] = items[j]
            j = j - 1
        items[j + 1] = key
    return items

res = insertion_sort([8,3,4,6,2,7,9,1])
print(res)