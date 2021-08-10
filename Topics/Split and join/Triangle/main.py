height = int(input())
for i in range(1, 1 + 2 * height, 2):
    print(("#" * i).center(2 * height - 1))
