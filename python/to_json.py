import csv
import json

input_csv = "Assets Icon List - data.csv"
output_json = "data.json"

data = []
with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # If tags are comma-separated in the CSV, split them, else edit as needed
        tags = [t.strip() for t in (row['tags (3)'] if 'tags (3)' in row else row['tags']).split(',') if t]
        item = {
            "filename": row['filename'],
            "slug": row['slug'],
            "name": row['name'],
            "tags": tags,
            "description": row['description']
        }
        data.append(item)

with open(output_json, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=2, ensure_ascii=False)

print(f"Converted {input_csv} to {output_json} with {len(data)} items.")
