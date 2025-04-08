def main():
    n, m = map(int, input().split())
    red = [0] + list(map(int, input().split()))
    blue = [0] + list(map(int, input().split()))
    
    count = 0
    
    # Check crossings
    for i in range(n):
        for j in range(m):
            if i % 2 == j % 2:
                if (red[i] < blue[j] and red[i+1] > blue[j+1]) or (red[i] > blue[j] and red[i+1] < blue[j+1]):
                    count += 1
            else:
                if (red[i] < blue[j+1] and red[i+1] > blue[j]) or (red[i+1] < blue[j] and red[i] > blue[j+1]):
                    count += 1

    # Check for touching points
    for i in range(n + 1):
        for j in range(i % 2, m + 1, 2):
            if red[i] == blue[j]:
                count += 1

    print(count)

if __name__ == "__main__":
    main()
