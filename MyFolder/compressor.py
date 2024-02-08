import os
import shutil
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    folder_name = os.path.basename(folder_path)
    current_date = datetime.now().strftime("%Y_%m_%d")
    compressed_filename = f"{folder_name}_{current_date}.{compress_type}"
    
    try:
        if compress_type == 'zip':
            with zipfile.ZipFile(compressed_filename, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), folder_path))
        elif compress_type == 'tar':
            with tarfile.open(compressed_filename, 'w') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == 'tgz':
            with tarfile.open(compressed_filename, 'w:gz') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            print("Unsupported compression type")
            return
        
        print(f"Compression successful. Compressed file saved as '{compressed_filename}'")
    except Exception as e:
        print(f"Compression failed: {str(e)}")

def get_folder_to_compress():
    folder_path = input("Enter the path of the folder to compress: ").strip()
    if not os.path.exists(folder_path):
        print("Folder not found.")
        return None
    return folder_path

def get_compression_type():
    compress_types = ['zip', 'tar', 'tgz']
    print("Available compression types:")
    for idx, ctype in enumerate(compress_types, start=1):
        print(f"{idx}. {ctype}")
    compress_choice = input("Select the compression type (enter the corresponding number): ").strip()
    try:
        compress_choice = int(compress_choice)
        if 1 <= compress_choice <= len(compress_types):
            return compress_types[compress_choice - 1]
        else:
            print("Invalid compression type selection.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def main():
    folder_path = get_folder_to_compress()
    if folder_path:
        compress_type = get_compression_type()
        if compress_type:
            compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()

