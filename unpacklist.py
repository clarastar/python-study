# date, name, price = ['December', 'Bread Glove', 8.51]
# print(name)
# print(date)

def drop_first_last(grades):
    first, *middle, last = grades
    print(len(middle))
    print(sum(middle))
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([5, 8, 4, 2, 1, 4])
