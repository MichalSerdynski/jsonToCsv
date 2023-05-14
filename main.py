import json
import csv

# Open the JSON file and load the data
with open('main_dataset copy.json') as f:
    data = json.load(f)

# Create a CSV file and write the headers
with open('suicide_deaths.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(
        ['id', 'uuid', 'position', 'created_at', 'created_meta', 'updated_at', 'updated_meta', 'meta', 'indicator',
         'indicator_description', 'geo_type', 'geo_name', 'geo_id', 'variable', 'time_period', 'time_period_label',
         'value', 'footnote'])

    # Write each row of data to the CSV file
    for row in data:
        writer.writerow(row)
