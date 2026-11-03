def lru_simulation():
    capacity = 3
    sequence = [4, 2, 1, 4, 3, 2, 5, 4]
    cache = []
    hits = 0

    print(f"{'Requested':<10}{'Status':<8}{'Evicted':<10}{'Cache'}")
    print("-" * 38)

    for page in sequence:
        evicted = "-"
        if page in cache:
            hits += 1
            status = "HIT"
            cache.remove(page)
            cache.append(page)
        else:
            status = "MISS"
            if len(cache) >= capacity:
                evicted = str(cache.pop(0))
            cache.append(page)
        print(f"{page:<10}{status:<8}{evicted:<10}{cache}")

    total = len(sequence)
    misses = total - hits
    hit_ratio = hits / total

    print("-" * 38)
    print(f"Total Hits: {hits}")
    print(f"Total Misses: {misses}")
    print(f"Hit Ratio: {hit_ratio:.2f}")

if __name__ == "__main__":
    lru_simulation()