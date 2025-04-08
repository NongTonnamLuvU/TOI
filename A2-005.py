def main():
    w, h = map(int, input().split())
    m, n = map(int, input().split())

    x = [0] + list(map(int, input().split())) + [w]
    y = [0] + list(map(int, input().split())) + [h]

    widths = [x[i+1] - x[i] for i in range(m + 1)]
    heights = [y[i+1] - y[i] for i in range(n + 1)]

    areas = [width * height for width in widths for height in heights]
    areas.sort(reverse=True)

    largest = areas[0]
    second_largest = areas[1] if len(areas) > 1 else largest

    print(largest, second_largest)

if __name__ == "__main__":
    main()
