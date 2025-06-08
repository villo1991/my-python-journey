#! python3
#bulletPointAdder.py - Aggunge punti elenco per Wikipedia
#all'inizio di ogni riga di testo negli Appunti.

import pyperclip
text= pyperclip.paste()

# Separa le righe e aggiunge gli asterischi.
lines= text.split('\n')
for i in range(len(lines)):
    lines[i]='#'+ lines[i]
text= "\n".join(lines)


pyperclip.copy(text)
