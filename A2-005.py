def main():
    W, H, M, N = map(int, input().split())
    x_cuts = list(map(int, input().split()))
    y_cuts = list(map(int, input().split()))

    x_positions = [0] + x_cuts + [W]
    y_positions = [0] + y_cuts + [H]

    widths = [x_positions[i+1] - x_positions[i] for i in range(len(x_positions) - 1)]
    heights = [y_positions[i+1] - y_positions[i] for i in range(len(y_positions) - 1)]

    areas = [w * h for w in widths for h in heights]
    areas.sort(reverse=True)

    max1 = areas[0]
    max2 = areas[1] if len(areas) > 1 else max1

    print(max1, max2)

if __name__ == "__main__":
    main()
