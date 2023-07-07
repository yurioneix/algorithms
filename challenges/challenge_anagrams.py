def is_anagram(first_string, second_string):
    # if first_string == "" or second_string == "":
    #     return (first_string, second_string, False)

    first = [char for char in first_string.lower()]
    second = [char for char in second_string.lower()]

    first_sorted = quick_sort(first, 0, len(first) - 1)
    second_sorted = quick_sort(second, 0, len(second) - 1)

    first_sorted_and_joined = "".join(first_sorted)
    second_sorted_and_joined = "".join(second_sorted)
    # print(first_sorted_and_joined)
    # print(first_sorted_and_joined)

    if not first_sorted_and_joined and not second_sorted_and_joined:
        return (first_sorted_and_joined, second_sorted_and_joined, False)
    if first_sorted_and_joined == second_sorted_and_joined:
        return (first_sorted_and_joined, second_sorted_and_joined, True)
    return (first_sorted_and_joined, second_sorted_and_joined, False)


# Quick sort implementado no Course
def quick_sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)
    return string


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):

        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = (
                string[delimiter],
                string[index],
            )

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1
