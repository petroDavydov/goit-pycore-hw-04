def total_salary(path):
    total_salary = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            salary_data = [line.strip() for line in file.readlines()]

    except FileNotFoundError:
        print("File not Found")

    for item in salary_data:
        person_sep_str = item.split(",")
        person_salery = int(person_sep_str[1])

        total_salary += person_salery

    average_salery = int(total_salary / len(salary_data))
    return (total_salary, average_salery)


total, average = total_salary("salary.txt")
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
