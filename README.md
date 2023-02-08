# Convert syntax highlighting from vscode to latex lstlistings

This python script converts the html code from vscode with syntax highlighting to a latex lstlisting.

## Dependencies
- [Clipview](http://www.peterbuettner.de/develop/tools/clipview/) for extracting the html code from the copied vscode text
- [Beautiful soup 4](https://pypi.org/project/beautifulsoup4/) for parsing the html code (Install with `pip3 install beautifulsoup4`)

## Usage
- Copy the syntax highlighted code from vscode to the clipboard
- Open Clipview, press view and then under format select `49382: HTML Format` to view the copied html code
![Screenshot of the Clipview software](images/clipview.png?raw=true)
- Copy the html format, create a new file and paste the copied html code into it
- Call `python3 convert.py path/to/html/file.html path/to/lstlisting/file.cpp` to convert the file
- Put `\lstinputlisting[language=C++,caption=Caption, captionpos=b, escapeinside={<@}{@>}]{path/to/lstlisting/file.cpp}` into your latex code to include the file
- The package `xcolor` must be included for color support