from pathlib import Path
lines = Path('index.html').read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines[904:910], start=904):
    print(i+1, repr(line))
