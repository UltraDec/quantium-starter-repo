import csv

with open('task2complete.csv', mode='w', newline='') as csv_write:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(csv_write, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(3):
        with open(f'./data/daily_sales_data_{i}.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == "pink morsel":
                    writer.writerow({'sales': f'{float(row[1][1:]) * int(row[2])}', 'date': row[3], 'region': row[4]})

    