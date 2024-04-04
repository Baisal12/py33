import csv

with open('file.csv') as a:
    r = csv.reader(a)
    for i in r:
        print(i)


'>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<'

data = [
    ['Name', 'Age', 'Profession'],
    ['Alice', 30, 'Engineer'],
    ['BoB', 40, 'Teacher'],
    ['Charlie', 25, 'Doctor']
]

with open('file.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    