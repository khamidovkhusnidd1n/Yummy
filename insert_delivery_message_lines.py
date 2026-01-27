from pathlib import Path
path = Path('index.html')
lines = path.read_text(encoding='utf-8').splitlines()
for idx, line in enumerate(lines):
    if "confirmMsg += `\\n??" in line:
        lines.insert(idx, "            if (deliveryMessage) {")
        lines.insert(idx + 1, "                confirmMsg += `?? ${deliveryMessage}\\n`;")
        lines.insert(idx + 2, "            }")
        break
else:
    raise SystemExit('confirm final line not found')
path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('delivery note inserted next to confirm')
