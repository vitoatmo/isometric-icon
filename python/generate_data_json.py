import os
import json

img_folder = './renamed-images'
old_json_path = './old_data.json'
new_json_path = './data.json'

# Baca data.json lama
try:
    with open(old_json_path, 'r') as f:
        old_data = json.load(f)
except:
    old_data = []

# Index filename -> metadata
meta_dict = {item['filename'].lower(): item for item in old_data if 'filename' in item}

# Scan semua .png
new_data = []
for filename in os.listdir(img_folder):
    if filename.endswith('.png'):
        key = filename.lower()
        # Pakai metadata lama kalau ada
        if key in meta_dict:
            item = meta_dict[key]
        else:
            # Auto generate metadata baru
            slug = filename.replace('.png', '')
            name = slug.replace('-', ' ').title()
            item = {
                "filename": filename,
                "slug": slug,
                "name": name,
                "tags": ["animals"],  # Default tags, ganti sesuai kebutuhan
                "desc": ""            # Desc kosong, isi manual jika perlu
            }
        new_data.append(item)

# Output ke data.json baru
with open(new_json_path, 'w') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)

print(f'Done! Data untuk {len(new_data)} images sudah di-generate ke {new_json_path}')
