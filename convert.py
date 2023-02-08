import re
import sys
from bs4 import BeautifulSoup

assert len(sys.argv) >= 3, "Please provide the html filename and a lstlisting filename"
file = BeautifulSoup(open(sys.argv[1]), features="html.parser")
text_color = re.match("color: \#([0-9a-f]{6})", list(file.body.children)[2].get('style')).groups()[0]
lines = [list(div.children) for div in list(file.body.children)[2].children]

file_text = ""
for line in lines:
    for segment in line:
        color = re.match("color: \#([0-9a-f]{6})", segment.get('style')).groups()[0]
        text = segment.get_text().replace('\\', '\\textbackslash ').replace("#", "\\#").replace('"', "''").replace('  ', "\t").replace('{', '\\{').replace('}', '\\}').replace('[', '\\lbrack').replace(']', '\\rbrack').replace('_', '\\_').replace('&', '\\&')
        if text.strip() == "":
            file_text += text
            continue
        left_chars = text[:-len(text.lstrip())]
        right_chars = text[len(text.rstrip()):]
        if file_text.endswith("@>") and left_chars == "":
            file_text = file_text[:-2]
        else:
            file_text += f"{left_chars}<@"
        file_text += f"\\texttt{{\\textcolor[HTML]{{{color}}}{{{text.strip()}}}}}@>{right_chars}"
    file_text += "\n"
open(sys.argv[2], 'w+').write(file_text)