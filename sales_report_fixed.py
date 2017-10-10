def read_data(filename):
    with open(filename) as file_data:
        sales_by_person = {}
        for line in file_data:
            name, amount, number = line.rstrip().split('|')
            sales_by_person[name] = sales_by_person.get(name, 0) + int(number)
    return sales_by_person


def print_sales(file_data):
    for person in file_data:
        print "{person} sold {number} melons.".format(
            person=person, number=file_data[person])

file_data = read_data("sales-report.txt")
print_sales(file_data)
