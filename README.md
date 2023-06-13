# :file_folder: File Search Script

## :page_facing_up: Overview

The File Search Script is a Python script that allows you to search a specified folder and its subfolders, up to two levels deep, to compile a list of all `.jpg` files contained within. The script utilizes `for` loops, conditional statements, and the `pathlib` module to efficiently traverse the folder structure and extract the desired files.

## :gear: Functionality

The script offers the following functionality:

- Folder Search: The script searches a specified folder and its subfolders, up to two levels deep, to locate all `.jpg` files.
- File List Generation: The script compiles a list of the complete paths of each `.jpg` file found during the search.
- Extension Listing (Optional): If desired, the script can create a list containing each type of file extension found in the specified folder.

## :rocket: Usage

To use the File Search Script, follow these steps:

1. Specify the folder path: In the script, replace `your-folder-path` with the path to the folder you want to search.
2. Run the script: Execute the script using a Python interpreter.
3. View the results: The script will display the complete paths of all `.jpg` files found in the specified folder and its subfolders. Optionally, it will also list other file extensions encountered.

Please note that the File Search Script is written in Python and requires a Python interpreter to run.

## :bulb: Tips

- Start with a small folder: Begin by testing the script on a small folder to ensure it functions correctly. This allows for easy verification of the script's accuracy.
- Gradually increase folder size: Once you have confirmed the script's effectiveness, gradually search larger folders to ensure it can handle directories of varying sizes.

## :page_with_curl: License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
