x = int(input("write the KwH have use: "))
total_cost = 0
if x <= 50:
    total_cost = x * 1700
elif x <= 100:
    total_cost = (50 * 1700) + ((x - 50) * 1900)
elif x <= 200:
    total_cost = (50 * 1700) + (50 * 1900) + ((x - 100) * 2100)
else:
    total_cost = (50 * 1700) + (50 * 1900) + (100 * 2100) + ((x - 200) * 3000)

print(f"Total electricity cost: {total_cost} VND")