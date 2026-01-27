from pathlib import Path
lines = Path('index.html').read_text(encoding='utf-8').splitlines()
print('\n'.join(lines[904:911]))
