from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = "            confirmMsg += `\n?? Jami: ${finalTotal.toLocaleString()} so'm`;\n"
new = "            if (deliveryMessage) {\n                confirmMsg += `?? ${deliveryMessage}\n`;\n            }\n            confirmMsg += `\n?? Jami: ${finalTotal.toLocaleString()} so'm`;\n"
if old not in text:
    raise SystemExit('footer line not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
print('delivery message appended to confirm')
