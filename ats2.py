def calculate_eat(h, tlb, mem):
    return h * (tlb + mem) + (1 - h) * (tlb + 2 * mem)

def main():
    tlb_time = 10   # in ns
    mem_time = 80   # in ns

    # Given parameters
    print(f"TLB Lookup Time: {tlb_time} ns")
    print(f"Main Memory Access Time: {mem_time} ns")

    # Case 1: Hit ratio = 0.90
    h1 = 0.90
    eat1 = calculate_eat(h1, tlb_time, mem_time)
    print(f"\nHit Ratio: {h1} -> EAT: {eat1:.2f} ns")

    # Case 2: Hit ratio = 0.75
    h2 = 0.75
    eat2 = calculate_eat(h2, tlb_time, mem_time)
    print(f"Hit Ratio: {h2} -> EAT: {eat2:.2f} ns")

    # Comparison
    diff = eat2 - eat1
    print(f"\nComparison: Decreasing hit ratio increases EAT by {diff:.2f} ns.")

if __name__ == "__main__":
    main()