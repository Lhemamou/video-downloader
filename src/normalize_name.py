import os
import argparse
from pathlib import Path
import re

def normalize_filename(filename):
    """
    Normalize a filename by:
    - Converting to lowercase
    - Replacing spaces with underscores
    - Removing special characters
    - Preserving the original extension
    """
    # Split filename and extension
    name, ext = os.path.splitext(filename)
    
    # Convert to lowercase
    name = name.lower()
    ext = ext.lower()
    
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    
    # Remove special characters but keep underscores
    name = re.sub(r'[^a-z0-9_]', '', name)
    
    # Remove multiple consecutive underscores
    name = re.sub(r'_+', '_', name)
    
    # Remove leading/trailing underscores
    name = name.strip('_')
    
    # Combine name and extension
    return f"{name}{ext}" if name else f"file{ext}"

def normalize_files(input_folder, recursive=False):
    """
    Normalize all filenames in the given folder.
    
    Args:
        input_folder (str): Path to folder containing files
        recursive (bool): Whether to process subfolders recursively
    """
    if recursive:
        # Use os.walk for recursive processing
        for root, dirs, files in os.walk(input_folder):
            process_files_in_folder(root, files)
    else:
        # Process only files in the input folder
        files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
        process_files_in_folder(input_folder, files)

def process_files_in_folder(folder, files):
    """
    Process files in a single folder.
    """
    for filename in files:
        old_path = os.path.join(folder, filename)
        new_filename = normalize_filename(filename)
        
        if new_filename != filename:
            new_path = os.path.join(folder, new_filename)
            counter = 1
            
            # Handle filename conflicts
            while os.path.exists(new_path):
                name, ext = os.path.splitext(new_filename)
                new_path = os.path.join(folder, f"{name}_{counter}{ext}")
                counter += 1
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {os.path.basename(new_path)}")
            except OSError as e:
                print(f"Error renaming {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='Normalize filenames in a folder by removing special characters and converting to lowercase'
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input folder containing files to rename',
        type=str,
        dest='input_folder'
    )
    
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Process subfolders recursively',
        default=False
    )
    
    parser.add_argument(
        '-d', '--dry-run',
        action='store_true',
        help='Show what would be done without making changes',
        default=False
    )

    args = parser.parse_args()
    
    # Validate input folder
    if not os.path.isdir(args.input_folder):
        parser.error(f"Input folder '{args.input_folder}' does not exist")
    
    normalize_files(args.input_folder, args.recursive)

if __name__ == "__main__":
    main()