import os
from create_parking_lot import create_parking_lot
from park import park
from leave import leave


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
                self.cars_arrived, self.cars_parked,
                self.currently_parked = park(
                        cmd[1], cmd[2], self.cars_arrived,
                        self.cars_parked, self.currently_parked)
            else:
                print("Invalid command")
                return

        elif cmd[0] == "leave":
            if len(cmd) == 2:
                self.currently_parked = leave(cmd[1], self.currently_parked)
            else:
                print("Invalid command")
                return

        elif cmd[0] == "status":
            if len(cmd) == 1:
                status(self.currently_parked)
            else:
                print("Invalid command")
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
