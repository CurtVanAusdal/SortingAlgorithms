insert_counter = 0
insert_counter2 = 0
selec_comparisons = 0
selec_swaps = 0
merge_comp = 0
merge_swap = 0
quick_comp = 0
quick_swap = 0


def is_sorted(lyst):
    # see if the list is already sorted

    if type(lyst) != list:
        raise TypeError('This is bad')

    elif type(lyst) == list:
        for i in range(len(lyst)):
            if type(lyst[i]) != int:
                raise TypeError('This is bad')

        for i in range(len(lyst) - 1):

            if lyst[i + 1] < lyst[i]:
                # it's notsorted if it does this even once

                return False

        return True
    else:
        return True


def quicksort(lyst):
    listy = lyst

    def sort_it(lyst):

        global quick_swap
        global quick_comp
        quick_comp = quick_comp + 1
        if (len(lyst)) <= 1:
            return lyst

        else:
            pivotdex = (len(lyst) - 1) // 2
            pivotval = (lyst[pivotdex])
            # print(pivotdex)
            pivot = lyst.pop(pivotdex)
            pivotlist = [pivot]
        biglist = []
        smalllist = []

        for i in lyst:
            quick_swap = quick_swap + 1
            if i > pivot:
                biglist.append(i)
            else:
                smalllist.append(i)

        # iterate_this = quicksort(smalllist) + pivotlist + quicksort(biglist)
        # print(pivotvallist,'pivot value')
        # print(biglist,'biglist')
        # print(smalllist,'smalllist')

        return sort_it(smalllist) + pivotlist + sort_it(biglist)

    return ((sort_it(listy)), quick_comp, quick_swap)


def selection_sort(lyst):
    # don't change anything it works
    global selec_comparisons
    global selec_swaps

    if type(lyst) != list:
        raise TypeError('This is bad')

    for index in range(len(lyst) - 1):
        minndex = index
        for j in range(index + 1, len(lyst)):
            selec_swaps += 1
            if lyst[minndex] > lyst[j]:
                minndex = j
        selec_comparisons += 1
        storage = lyst[index]  # store value of the first index
        lyst[index] = lyst[minndex]
        lyst[minndex] = storage
    # print(lyst)
    return (lyst, selec_comparisons, selec_swaps)


def insertion_sort(lyst):
    # insertion sort algorythm sorts the list and counts swaps and comparisons
    global newlist
    newlist = lyst

    global insert_counter
    global insert_counter2

    insert_counter += 1
    if type(lyst) != list:
        raise TypeError('This is bad')

    for index in range(len(lyst) - 1):
        current = index + 1
        if lyst[current] < lyst[current - 1]:
            # do something! Move index to the right and put current where index was
            # num_list.insert(index, num)
            stored_value = lyst[current]
            # print(stored_value)
            lyst[current] = lyst[index]
            lyst[index] = stored_value
            # print(lyst)
            insert_counter2 += 1  # counting swaps
        # while is_sorted(newlist) == False:
        #     insertion_sort(lyst) # i am using recursion
        #     # elif is_sorted(lyst) == True:
        #     #     return
        elif lyst[current] > lyst[index]:
            # don't do anything, keep moving
            pass

    while is_sorted(newlist) == False:
        insertion_sort(lyst)  # i am using recursion
    # elif is_sorted(lyst) == True:
    #     return

    return (lyst, insert_counter, insert_counter2)


def mergesort(lyst):
    global merge_comp
    global merge_swap

    if type(lyst) != list:
        raise TypeError('This is bad')

    splitlist = []

    def sort_j(lyst):
        for index in range(len(lyst) - 1):
            minndex = index
            for j in range(index + 1, len(lyst)):
                global merge_swap
                # merge_swap +=1
                if lyst[minndex] > lyst[j]:
                    minndex = j

            storage = lyst[index]  # store value of the first index
            lyst[index] = lyst[minndex]
            lyst[minndex] = storage
        # print(lyst)
        return (lyst)

    def split(lyst):

        if len(lyst) == 1:
            splitlist.append(lyst)

        else:
            # I thought the the following would only work in matlab but it seems to be working so keep going
            middledex = len(lyst) // 2
            half1 = lyst[:middledex]
            half2 = lyst[middledex:]
            # print(half1)
            # print(half2)
            split(half1)
            split(half2)

        return (splitlist)

    def mergeit(lyst):
        newlist = []

        if type(lyst) != list:
            raise TypeError('This is bad')

        if len(newlist) != 1:
            for i in range(len(lyst) - 1):
                if i % 2 == 0:
                    newlist.append(lyst[i] + lyst[i + 1])
            if len(lyst) % 2 != 0:
                newlist.append(lyst[-1])

            for i in newlist:
                global merge_swap
                merge_swap += 1
                for index in i:
                    sort_j(i)
            global merge_comp
            merge_comp += 1
            # print(newlist)
            # print(len(newlist))

            if len(newlist) == 1:
                global final
                final = newlist
                global final_sorted
                final_sorted = final[0]





            else:
                (mergeit(newlist))

        return (final_sorted, merge_comp, merge_swap)

    splitit = split(lyst)
    # print(splitlist)
    final_lyst = (mergeit(splitlist))

    return (final_lyst)


def main():
    lyst = [2, 6, 5, 3, 100, 90, 80, 40, 140, 223, 2, 30, 2, 33, 10, 0, 1, 44, 22, 99, 101, 87]
    print(lyst)
    # print(is_sorted(lyst))
    print('output is: [sorted list], Number of comparisons, Number of swaps ')
    print(insertion_sort(lyst))
    print(selection_sort(lyst))
    print(mergesort(lyst))
    print(quicksort(lyst))


if __name__ == "__main__":
    main()
