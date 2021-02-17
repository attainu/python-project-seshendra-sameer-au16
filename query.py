from tabulate import tabulate


def status(currently_parked):
    vals = []
    for key, value in currently_parked.items():
        if value is not False:
            vals.append([key, value[0], value[1]])

    headers = ['slot', 'registration_no', 'color']

    print(tabulate(vals, headers))


def registration_numbers_for_cars_with_color(color, cars_arrived):
    temp = []
    for i in cars_arrived:
        if i[1] == color:
            temp.append(i[0])

    if len(temp) == 0:
        print("No %s car has entered this parking lot" % color)
        return
    for i in temp[:len(temp) - 1]:
        print(i, end=", ")
    print(temp[-1])


def slot_numbers_for_cars_with_color(color, currently_parked):
    temp = []
    for key, value in currently_parked.items():
        if value is not False:
            if value[1] == color:
                temp.append(key)

    if len(temp) == 0:
        print("Not found")
        return
    for i in temp[:len(temp) - 1]:
        print(i, end=", ")
    print(temp[-1])


def slot_number_for_cars_with_registration_number(registration_no, currently_parked):
    temp = []
    for key, value in currently_parked.items():
        if value is not False: 
            if value[0] == registration_no:
                temp.append(key) 

    if len(temp) == 0:
        print("Not found")
        return
    for i in temp[:len(temp) - 1]:
        print(i, end = ", ")
    print(temp[-1])
