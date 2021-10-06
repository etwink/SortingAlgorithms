def reverseList(size):
    worstCaseList = list()
    for i in range(size, 0, -1):
        worstCaseList.append(i)
    return worstCaseList