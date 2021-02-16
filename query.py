from tabulate import tabulate


def status(currently_parked):
    vals = []
    for key, value in currently_parked.items():
        if value is not False:
            vals.append([key, value[0], value[1]])
    headers = ['slot', 'reg_no', 'color']

    print(tabulate(vals, headers))


def registration_numbers_for_cars_with_colour(color, cars_arrived):
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
