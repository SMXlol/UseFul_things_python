def insertion_sort(unsorted, n):
    for i in range(1, n):
        val = unsorted[i].value
        hole = i
        while hole > 0 and unsorted[hole - 1].value > val:
            unsorted[hole].value = unsorted[hole - 1].value
            hole -= 1
        unsorted[hole].value = val

insertion_sort(random_list_of_nums4, 1)
