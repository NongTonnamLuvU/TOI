def main():
    nums = list(map(int, input().split()))
    visited = set()
    ans = []

    for x in nums:
        if x not in visited:
            visited.add(x)
            ans.append(x)

    print(*ans)

if __name__ == "__main__":
    main()
