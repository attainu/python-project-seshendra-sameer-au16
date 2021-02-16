import os


if __name__ == "__main__":
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
                        solve(line.strip().split())
                break
            except:
                continue
        else:
            try:
                solve(cmd.strip().split())
            except:
                continue