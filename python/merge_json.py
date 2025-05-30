import json

# Load animals.json
with open('data/animals.json', 'r') as f:
    animals = json.load(f)

# Load dog.json
with open('data/dog.json', 'r') as f:
    dogs = json.load(f)

# Merge (combine the lists)
merged_data = animals + dogs

# Write to data.json
with open('data/data.json', 'w') as f:
    json.dump(merged_data, f, indent=2)

print('Merged data saved to data/data.json')
