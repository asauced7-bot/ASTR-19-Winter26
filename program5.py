import math

def main():
    start = 0.0
    end = 2.0
    num_entries = 1000

    step = (end - start) / (num_entries - 1)

    print("x\t\tsin(x)")
    print("----------------------")

    for i in range(num_entries):
        x = start + i * step
        y = math.sin(x)
        print(f"{x:.6f}\t{y:.6f}")

if __name__ == "__main__":
    main()