#! python3

import pyperclip
text= pyperclip.paste()

lines= text.split('\n')
for i in range(len(lines)):
    lines[i]= lines[i][1:]
text= "\n".join(lines)

pyperclip.copy(text)
