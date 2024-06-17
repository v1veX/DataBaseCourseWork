import csv


def write(filename, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(data)


def read_all(filename):
    rows = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            rows.append(row)
    return rows
