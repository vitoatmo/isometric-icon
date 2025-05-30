import os
import shutil

src_folder = './04_dogs'            # folder asal
dst_folder = './renamed-images'    # folder tujuan

# Bikin folder tujuan kalau belum ada
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

for filename in os.listdir(src_folder):
    if filename.endswith('.png'):
        # Lowercase, ganti spasi ke dash, hapus karakter tidak aman
        new_name = filename.lower().replace(' ', '-').replace('--', '-')
        new_name = ''.join(c for c in new_name if c.isalnum() or c in ['-', '.'])
        
        src_path = os.path.join(src_folder, filename)
        dst_path = os.path.join(dst_folder, new_name)
        
        shutil.copy2(src_path, dst_path)  # copy file (bisa juga shutil.move untuk pindah)
        print(f'Copied: {filename} -> {new_name}')
