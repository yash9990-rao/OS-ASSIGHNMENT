class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid  # Process ID
        self.at = at    # Arrival Time
        self.bt = bt    # Burst Time
        self.ct = 0     # Completion Time
        self.tat = 0    # Turnaround Time
        self.wt = 0     # Waiting Time

def get_input():
    processes = []
    n = int(input("Enter number of processes (4-5 recommended): "))
    for i in range(n):
        print(f"\nProcess {i+1}:")
        pid = input("Enter PID: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append(Process(pid, at, bt))
    return processes

def display_table(processes, title):
    print(f"\n--- {title} ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")