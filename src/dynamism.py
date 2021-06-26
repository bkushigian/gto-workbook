from sys import argv, exit

def variance(xs):
    mean = sum(xs) / len(xs)
    deviations = [(x - mean) **2 for x in xs]
    return sum(deviations) / len(deviations)

def dynamism(xs, pot):
    return 1000 * variance(xs)**0.5 / pot

def main():
    if len(argv) != 4:
        print("usage: dynamism file ev-index pot")
        exit(1)

    ev_index = int(argv[2])
    with open(argv[1]) as f:
        evs = [float(line.split()[ev_index]) for line in f.readlines()]
        print(dynamism(evs, float(argv[3])))

if __name__ == "__main__":
    main()