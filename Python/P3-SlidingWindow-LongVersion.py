# Sliding Window Protocol
# Go-Back-N and Selective Repeat
# A lost frame can be entered for every window


def read_lost_frame(start, end):
    while True:
        lost = int(input("Enter lost frame (0 for none): "))
        if lost == 0 or start <= lost <= end:
            return lost
        print("Lost frame must be 0 or between", start, "and", end)


def go_back_n(total, window):
    print("\n--- Go-Back-N Protocol ---")
    start = 1
    while start <= total:
        end = min(start + window - 1, total)
        print("\nSending frames:", *range(start, end + 1))
        lost = read_lost_frame(start, end)

        if lost == 0:
            print("All frames received successfully. ACK", end)
            start = end + 1
        else:
            print("Frame", lost, "is lost. ACK not received (timeout).")
            if lost > start:
                print("ACK received for frames", start, "to", lost - 1)
            print("Frames", lost, "to", end, "are discarded by receiver")
            print("Go-Back-N: Going back and retransmitting from frame", lost)
            start = lost

    print("\nTransmission completed.")


def selective_repeat(total, window):
    print("\n--- Selective Repeat Protocol ---")
    start = 1
    while start <= total:
        end = min(start + window - 1, total)
        print("\nSending frames:", *range(start, end + 1))
        lost = read_lost_frame(start, end)

        if lost == 0:
            print("All frames received successfully. ACK", end)
        else:
            print("Frame", lost, "is lost. ACK not received (timeout).")
            others = [f for f in range(start, end + 1) if f != lost]
            if others:
                print("Selective Repeat: Frames", *others, "are buffered at receiver")
            print("  Retransmitting only frame", lost)
            print("Frame", lost, "received. ACK received for frames", start, "to", end)

        start = end + 1

    print("\nTransmission completed.")


while True:
    print("\n========== SLIDING WINDOW PROTOCOL ==========")
    print("1. Go-Back-N")
    print("2. Selective Repeat")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 3:
        print("Program terminated.")
        break

    if choice not in (1, 2):
        print("Invalid choice.")
        continue

    total = int(input("Enter total frames: "))
    window = int(input("Enter window size: "))

    if choice == 1:
        go_back_n(total, window)
    else:
        selective_repeat(total, window)
