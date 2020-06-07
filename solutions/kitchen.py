
salads = [
    {"id": 1, "name": "Caesar", "price": 8.99},
    {"id": 2, "name": "Chicken Caesar", "price": 11.99},
    {"id": 3, "name": "Waldorf", "price": 10.99},
    {"id": 4, "name": "Cobb", "price": 9.99},
    {"id": 5, "name": "Caprese", "price": 9.99},
    {"id": 6, "name": "Nicoise", "price": 10.99},
]

if __name__ == "__main__":

    print("------------------")
    print("PROCESSING KITCHEN DATA...")
    print("------------------")
    # print(salads)


# breakpoint()

#
# QUESTION A
#
# Assuming the identifier, or "id" attribute, of each salad is and will always be unique,
# ... and assuming the order of salads may vary,
# ... "print" the name of the salad whose identifier is equal to 3 (i.e. "Waldorf"):


for s in salads:
    if s["id"] == 3:
        print(s["name"])

salad = [p for p in salads if p["id"] == 3]
salad_1 = salad[0]
print(salad_1["name"])

print([s["name"] for s in salads if s["id"] == 3])
print([s["name"] for s in salads if s["id"] == 3][0])


#
# QUESTION B
#
# Assuming the "price" attribute represents a salad’s cost to the consumer,
# ... "print" the number of salads which are more expensive than ten dollars (i.e. 3):

salads_expensive = []

for s in salads:
    price = s["price"]
    if price > 10:
        salads_expensive.append(s)

print(len(salads_expensive))
