# Sliding Window Protocol
# Go-Back-N and Selective Repeat

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
    lost = int(input("Enter lost frame (0 for none): "))

    start = 1
    while start <= total:
        end = min(start + window - 1, total)
        print("\nSending frames:", *range(start, end + 1))

        if start <= lost <= end:
            print("Frame", lost, "is lost. ACK not received (timeout).")

            if choice == 1:
                print("Go-Back-N: Retransmitting frames", lost, "to", end)
                for i in range(lost, end + 1):
                    print("  Retransmitting frame", i)
            else:
                print("Selective Repeat: Frames other than", lost, "are buffered at receiver")
                print("  Retransmitting frame", lost)

            lost = 0
            print("ACK received for frames", start, "to", end)
        else:
            print("All frames received successfully. ACK", end)

        start = end + 1

    print("\nTransmission completed.")
