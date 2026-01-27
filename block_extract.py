from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
start = text.index("            confirmMsg += `??")
end = text.index("\n\n            if (!confirm", start)
print(text[start:end])
