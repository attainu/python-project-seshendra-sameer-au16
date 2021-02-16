from tabulate import tabulate


def status(currently_parked):
    vals = []
    for key, value in currently_parked.items():
        if value is not False:
            vals.append([key, value[0], value[1]])
    headers = ['slot', 'reg_no', 'color']

    print(tabulate(vals, headers))
