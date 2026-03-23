import sys
import pyperclip

TOTAL_LENGTH = 80
PREFIX = '// ─── '
SUFFIX = ' '
FILL = '─'
END = '─'

def generate_break(label: str) -> str:
    fixed_parts = PREFIX + label + SUFFIX
    remaining = TOTAL_LENGTH - len(fixed_parts) - len(END)
    fill = FILL * max(0, remaining)
    return f"{PREFIX}{label}{SUFFIX}{fill}{END}"

if len(sys.argv) < 2:
    print('Usage: python generateBreak.py "My Section Label"')
    sys.exit(1)

label = sys.argv[1]
result = generate_break(label)
print(result)
pyperclip.copy(result)
print("Copied to clipboard")