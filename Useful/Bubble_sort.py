def bubble_sort(arr_num):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr_num) - 1):
            if arr_num[i] > arr_num[i + 1]:
                arr_num[i], arr_num[i + 1] = arr_num[i + 1], arr_num[i]
                flag = True

bubble_sort(random_list_of_nums2)
