
def get_cats_info(path):

    result_cat = []
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_list = [line.strip() for line in file.readlines()]

    except FileNotFoundError:
        print(f"File not Found!")
        return result_cat

    for i in cats_list:
        item = i.split(",")
        cat = {"id": item[0], "name": item[1], "age": int(item[2])}
        result_cat.append(cat)

    return result_cat


cats_info = get_cats_info("cats.txt")
print(cats_info)


# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
