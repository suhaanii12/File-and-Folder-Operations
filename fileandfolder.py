import os
import shutil

def create_file(file_path, content):
    """Create a new file with the given content."""
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File created: {file_path}")

def create_folder(folder_path):
    """Create a new folder."""
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder created: {folder_path}")

def move_file(src, dst):
    """Move a file from src to dst."""
    shutil.move(src, dst)
    print(f"File moved from {src} to {dst}")

def move_folder(src, dst):
    """Move a folder from src to dst."""
    shutil.move(src, dst)
    print(f"Folder moved from {src} to {dst}")

def rename_file(src, dst):
    """Rename a file from src to dst."""
    os.rename(src, dst)
    print(f"File renamed from {src} to {dst}")

def rename_folder(src, dst):
    """Rename a folder from src to dst."""
    os.rename(src, dst)
    print(f"Folder renamed from {src} to {dst}")

def delete_file(file_path):
    """Delete a file."""
    os.remove(file_path)
    print(f"File deleted: {file_path}")

def delete_folder(folder_path):
    """Delete a folder and all its contents."""
    shutil.rmtree(folder_path)
    print(f"Folder deleted: {folder_path}")

# Example usage:

# Creating files and folders
create_file('example.txt', 'Hello, world!')
create_folder('example_folder')

# Moving files and folders
move_file('example.txt', 'example_folder/example.txt')
move_folder('example_folder', 'new_example_folder')

# Renaming files and folders
rename_file('new_example_folder/example.txt', 'new_example_folder/renamed_example.txt')
rename_folder('new_example_folder', 'renamed_example_folder')

# Deleting files and folders
delete_file('renamed_example_folder/renamed_example.txt')
delete_folder('renamed_example_folder')
