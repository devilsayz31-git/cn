# Leaky Bucket Algorithm for Congestion Control


def main():
    bucket_size = int(input("Enter bucket size: "))
    output_rate = int(input("Enter output rate: "))
    n = int(input("Enter number of time intervals: "))

    stored = 0
    total_dropped = 0
    total_sent = 0

    for i in range(1, n + 1):
        incoming = int(input(f"\nEnter packets arriving at time {i}: "))

        # Check for overflow
        if stored + incoming > bucket_size:
            dropped = (stored + incoming) - bucket_size
            print(f"Bucket overflow! Packets dropped: {dropped}")
            total_dropped += dropped
            stored = bucket_size
        else:
            stored += incoming

        transmitted = min(stored, output_rate)
        stored -= transmitted
        total_sent += transmitted
        print(f"Packets transmitted: {transmitted}")
        print(f"Packets remaining in bucket: {stored}")

    # Empty the remaining packets
    t = n
    while stored > 0:
        t += 1
        transmitted = min(stored, output_rate)
        stored -= transmitted
        total_sent += transmitted
        print(f"\nTime {t} (no new packets)")
        print(f"Packets transmitted: {transmitted}")
        print(f"Packets remaining: {stored}")

    print(f"\nTotal packets transmitted: {total_sent}")
    print(f"Total packets dropped: {total_dropped}")


if __name__ == "__main__":
    main()
