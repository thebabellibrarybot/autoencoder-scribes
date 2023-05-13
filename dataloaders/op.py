import csv

with open('data.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    for row in reader:
        writer.writerow(row[:-1])