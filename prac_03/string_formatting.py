# Use f-string formatting for the first output
brand = "Gibson"
model = "L-5 CES"
year = 1922
price = 16035.0

output1 = f"{year} {brand} {model} for about ${price:,.2f}!"
print(output1)

# Use a for loop with range and string formatting for the second output
for i in range(0, 201, 50):
    output2 = f"{i: >4}"
    print(output2)
