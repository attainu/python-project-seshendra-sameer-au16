import os
from create_parking_lot import create_parking_lot
from park import park
from leave import leave
from query import status
from query import registration_numbers_for_cars_with_color
from query import slot_numbers_for_cars_with_color
from query import slot_number_for_cars_with_registration_number


class Solution:
    def __init__(self):
        self.cars_arrived = []
        self.cars_parked = {}
        self.currently_parked = {}

    def solve(self, cmd):
        if cmd[0] == "create_parking_lot":
            if len(cmd) == 2:
                self.currently_parked = create_parking_lot(
                    int(cmd[1]), self.currently_parked)
            else:
                print("Invalid command")
                return

        elif cmd[0] == "park":
            if len(cmd) == 3:
                self.cars_arrived, self.cars_parked, self.currently_parked = park(
                        cmd[1], cmd[2], self.cars_arrived,
                        self.cars_parked, self.currently_parked)
            else:
                print("Invalid command")
                return

        elif cmd[0] == "leave":
            if len(cmd) == 2:
                self.currently_parked = leave(int(cmd[1]), self.currently_parked)
            else:
                print("Invalid command")
                return

        elif cmd[0] == "status":
            if len(cmd) == 1:
                status(self.currently_parked)
            else:
                print("Invalid command")
                return

        elif cmd[0] == "registration_numbers_for_cars_with_color":
            if len(cmd) == 2:
                registration_numbers_for_cars_with_color(
                    cmd[1], self.cars_arrived)
            else:
                print("Invalid command")
                return

        elif cmd[0] == "slot_numbers_for_cars_with_color":
            if len(cmd) == 2:
                slot_numbers_for_cars_with_color(
                    cmd[1], self.currently_parked)
            else:
                print("invalid command")
                return

        elif cmd[0] == "slot_number_for_cars_with_registration_number":
            if len(cmd) == 2:
                slot_number_for_cars_with_registration_number(
                    cmd[1], self.currently_parked)
            else:
                print("invalid command")
                return


if __name__ == "__main__":
    s = Solution()
    while True:
        cmd = input("$ ")
        if len(cmd) == 0:
            continue
        elif cmd == "exit":
            break
        elif cmd.endswith(".txt"):
            try:
                with open(cmd) as textfile:
                    for line in textfile:
                        line = line.rstrip("\n")
                        s.solve(line.strip().split())
                break
            except:
                continue
        else:
            try:
                s.solve(cmd.strip().split())
            except:
                continue
