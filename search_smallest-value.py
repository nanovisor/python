smallest = None
for i in [9, 41, 54, 1, 5]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    print smallest, i
