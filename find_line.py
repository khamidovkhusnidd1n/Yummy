from pathlib import Path
lines = Path('index.html').read_text(encoding='utf-8').splitlines()
for idx, line in enumerate(lines):
    if '\\n??' in line:
        print(idx, repr(line))
