import os
import sys
import time

def main():
    _, name, interval, executable = sys.argv
    execute_task(name, int(interval), executable)

def execute_task(name, interval, executable):
    while True:
        print(f"Doing: {name}")
        os.system(executable)
        time.sleep(interval)

if __name__ == "__main__":
    main()
