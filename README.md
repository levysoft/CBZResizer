# CBZ Resizer
Python script for efficiently resizing images within CBZ files with customizable compression settings, featuring added read-only support for CBR files

## Description
CBZ Resizer is a Python script developed to resize images within CBZ files. Users can specify a compression percentage to reduce image sizes, thus affecting the overall size of the CBZ file. It also offers read-only support for CBR files due to the rarfile library's limitation, which is a read-only library. Given this limitation and the script's primary focus on CBZ files, the project name remains "CBZ Resizer". For CBR files, the script can decompress the RAR archive, resize the images as required, and repack them into a new CBZ file.

## Features
- Resizes images within a CBZ file
- Read-only support for CBR files: decompresses CBR, resizes images, and converts to CBZ
- Customizable compression percentage
- Automatic output with "_resize" suffix

## Requirements
- Python 3.x
- PIL (Python Imaging Library), installable via `pip install Pillow`
- rarfile, installable via `pip install rarfile` (needed for CBR support)

## Installation
To set up the development environment:

1. Clone the repository:

   `git clone https://github.com/levysoft/CBZResizer`

2. Enter the project directory:

   `cd CBZResizer`

3. Create a Python virtual environment:

   `python3 -m venv venv`

4. Activate the virtual environment:

   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
5. Install dependencies:

   `pip install -r requirements.txt`

## Usage
To use the script, run the command:

`python3 cbz_resizer.py input_file [compression_percentage]`

Where input_file is the CBZ or CBR file to be processed and compression_percentage is an optional value indicating the compression level (0-100, default 50%).

## Contributing
Contributions are always welcome! Please follow these steps to contribute to the project:

1. Fork the repository.
2. Create a new branch: `git checkout -b branch_name`.
3. Make your changes and commit: `git commit -am 'Add some changes'`.
4. Push to the branch: `git push origin branch_name`.
5. Create a pull request.

## Note
This script was created for educational purposes and is not guaranteed for production use.

## Credits
This project was created by Antonio Troise.

## Acknowledgements
Special thanks to everyone who contributes to this project.

## Author
Antonio Troise

## License
This project is released under the MIT License. See the LICENSE file for more details.
