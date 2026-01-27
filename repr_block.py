from pathlib import Path
lines = Path('index.html').read_text(encoding='utf-8').splitlines()
block = '\n'.join(lines[905:910])
print(repr(block))
