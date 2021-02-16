def leave(slot, currently_parked):
    if currently_parked[slot] is not False:
        currently_parked[slot] = False
        print("Slot number %d is free" % slot)
    else:
        print("Token invalid")

    return currently_parked
