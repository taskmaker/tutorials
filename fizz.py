def result(i):
    end = i + 1
    for count in range(1, end):
        if count % 3 == 0:
            total = total + count
        elif count % 5 == 0:
            total = total + count
    return total