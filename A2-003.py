def main():
    n = int(input())
    tree = [0] + list(map(int, input().split())) + [0]  # Padding with zeros on both sides

    count = 0
    for i in range(1, n + 1):
        if tree[i] > tree[i - 1] and tree[i] > tree[i + 1]:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
