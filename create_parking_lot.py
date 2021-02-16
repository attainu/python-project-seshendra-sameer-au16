def create_parking_lot(slots, currently_parked):
    for i in range(1, slots + 1):
        currently_parked[i] = False
    print("Created a parking lot with %d slots" % slots)

    return currently_parked
