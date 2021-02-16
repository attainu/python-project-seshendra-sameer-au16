def park(registartion_no, color, cars_arrived, cars_parked, currently_parked):
    car = (registartion_no, color)
    cars_arrived.append(car)
    for key in currently_parked.keys():
        if currently_parked[key] is False:
            if car in cars_parked.keys():
                cars_parked[car].append(key)
            else:
                cars_parked[car] = [key]
            currently_parked[key] = car
            print("Allocated slot number: %d" % key)
            break
    else:
        print("Sorry, parking lot is full")

    return cars_arrived, cars_parked, currently_parked
