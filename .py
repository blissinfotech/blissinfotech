from PIL import Image
import os

def convert_image(input_path, output_path, output_format="webp"):
    try:
        image = Image.open(input_path)
        image.save(output_path, format=output_format)

    except Exception as e:
        print(f"Error: {e}")

import os

def list_files():
    folders=[]
    files=[]
    current_directory = os.getcwd()

    try:
        items = os.listdir(current_directory)
        for item in items:
            item_path = os.path.join(current_directory, item)
            if os.path.isfile(item_path):
                files.append(item)
            elif os.path.isdir(item_path):
                folders.append(item_path)
        return folders,files

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folders,files=list_files()
    print(folders,files)
