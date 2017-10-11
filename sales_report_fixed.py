def read_data_nested(filename):
    with open(filename) as file_data:
        name = None
        sales_by_person = {}
        for line in file_data:
            name, amount, number = line.rstrip().split('|')
            amount = float(amount)
            number = int(number)
            if name in sales_by_person.keys():
                sales_by_person[name]['price'] = sales_by_person[name]['price'] + amount
                sales_by_person[name]['number'] = sales_by_person[name]['number'] + number
            else:
                sales_by_person[name] = {'price': amount, 'number': number}
    return sales_by_person


def print_sales(file_data):
    for person in file_data:
        print "{person} sold {number:,} melons for ${amount:,.2f}.".format(
            person=person, number=file_data[person]['number'], amount=file_data[person]['price'])

file_data = read_data_nested("sales-report.txt")
print_sales(file_data)
