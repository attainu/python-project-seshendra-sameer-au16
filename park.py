def park(registartion_no, color, cars_arrived, cars_parked, currently_parked):
    car = (registartion_no, color)
    cars_arrived.append(car)
    for i in currently_parked.keys():
        if currently_parked[i] is False:
            if car in cars_parked.keys():
                cars_parked[car].append(i)
            else:
                cars_parked[car] = [i]
            currently_parked[i] = car
            print("Allocated slot number: %d" % i)
            break
    else:
        print("Sorry, parking lot is full")

    return cars_arrived, cars_parked, currently_parked
