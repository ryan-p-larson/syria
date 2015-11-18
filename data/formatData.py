import csv

refugees = {}
f = open("monthly-data-uncleaned.csv")

for row in csv.DictReader(f):
    key = row["Country"]
    refugees[key] = {}
    refugees[key]["Country"] = key

    for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"]:
        value = row[month]
        if value == " - ":
            value = 0
        elif value == " * ":
            value == 1
        refugees[key][month] = value       

with open("monthly-data.csv", "wb") as outfile:
    attrNames = refugees["Canada"].keys()
    print(attrNames)

    writer = csv.DictWriter(outfile, fieldnames = attrNames)
    writer.writeheader()

    for country in refugees:
        writer.writerow(refugees[country])

