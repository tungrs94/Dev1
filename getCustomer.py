import csv
from api import get_data

data = get_data()['customers']
keys = data[0].keys()
with open("data.csv", 'wt') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([key for key in keys])
    for info in data:
        writer.writerow([ i for i in info.values()])