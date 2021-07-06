from sys import argv, exit

def variance(xs):
    mean = sum(xs) / len(xs)
    deviations = [(x - mean) **2 for x in xs]
    return sum(deviations) / len(deviations)

def dynamism(xs, pot=1.0):
    return variance(xs)**0.5 / pot

def main():
    if len(argv) == 4:
        ev_index = int(argv[2])
        with open(argv[1]) as f:
            evs = [float(line.split()[ev_index]) for line in f.readlines()]
            print(dynamism(evs, float(argv[3])))
    elif len(argv) == 3:
        eq_index = int(argv[2])
        with open(argv[1]) as f:
            eqs = [line.split()[eq_index] for line in f.readlines()]
            if '%' not in eqs[0]:
                raise RuntimeError("Improper format: equities must end with '%'")
            eqs = [float(eq.strip(' %')) for eq in eqs]
            print(dynamism(eqs))
    else:
        print("usage: dynamism file ev-index pot")
        exit(1)


if __name__ == "__main__":
    main()