
n = int(input("Enter the number of rows: "))
print("\nPattern 1: Star Triangle")
print("------------------------")

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("Pattern 2: Number Triangle")
print("--------------------------")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("Pattern 3: Inverted Star Triangle")
print("---------------------------------")

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("Pattern 4: Pyramid")
print("-----------------")

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()