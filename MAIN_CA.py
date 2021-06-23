import FCFS_CPU
import PP_CPU
import SJFNP_CPU
import SJF_CPU
import PRIORITY_CPU
import ROUNDROBIN_CPU

def start():
    print("-----CPU SCHEDULING ALGORITHM-----")
    print("[1] First Come First Serve (FCFS)")
    print("[2] Shortest Remaining Time (SRT) Preemptive")
    print("[3] Shortest Job First (SJF) Non-preemptive")
    print("[4] Priority Queue Non-Preemptive")
    print("[5] Priority Queue Preemptive")
    print("[6] Round Robin") #quantum slice
    print("[7] Exit")
    print("----------------------------------")
    choice = input("Enter choice: ")
    choices(choice)


def choices(choice):
        if choice == "1":
            print("FIRST COME FIRST SERVE")
            FCFS_CPU.start()
            start()
        
        elif choice == "2":
            print("SHORTEST REMAINING TIME (PRE-EMPTIVE)") #preemptive
            SJF_CPU.start()
            start()

        # non preemptive
        elif choice == "3":
            print("SHORTEST JOB FIRST (NON- PREEMPTIVE)")  #non-preemptive
            SJFNP_CPU.start()
            start()

        elif choice == "4":
            print("PRIORITY (NON PRE-EMPTIVE)") #NON-PREEMPTIVE
            PRIORITY_CPU.start()
            start()

        # preemptive priority
        elif choice == "5":
            print("PRIORITY (PRE-EMPTIVE)") #PREEMPTIVE
            PP_CPU.start()
            start()

        elif choice == "6":
            print("ROUND ROBIN ")
            ROUNDROBIN_CPU.start()
            start()

        elif choice == "7":
            import sys
            sys.exit("Program terminated.")


        else:
            print("Invalid input.")

start()