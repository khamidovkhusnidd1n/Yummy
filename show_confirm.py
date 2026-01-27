import pathlib
lines = pathlib.Path('index.html').read_text(encoding='utf-8').splitlines()
print('\n'.join(lines[900:915]))
