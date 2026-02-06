def append(list1, list2):
    for num in list2:
        list1.append(num)
    return list1


def concat(lists):
    listing = []
    for num in lists:
        listing += num
    return listing


def filter(function, list):
    listing = []
    for num in list:
        if function(num) == True:
            listing.append(num)
    return listing


def length(list):
    return len(list)


def map(function, list):
    listing = []
    for num in list:
        listing.append(function(num))
    return listing


def foldl(function, list, initial):
    acc = initial
    for el in list:
        acc = function(acc, el)
    return acc


def foldr(function, list, initial):
    acc = initial
    for el in reversed(list):
        acc = function(acc, el)
    return acc


def reverse(list):
    list.reverse()
    return list
