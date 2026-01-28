''' First way
import os

if os.path.exists("File1.txt"):
    os.remove("File1.txt")
else:
    print("File not exist")
'''


''' Second way
from pathlib import Path

file = Path("File2.txt")
file.unlink(missing_ok=True)
'''

#Third way
import os

file = "File3.txt"

if os.path.exists(file):
    os.unlink(file)