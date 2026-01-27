from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = "            if (promoResult.valid && discount > 0) {\n                confirmMsg += `? Chegirma: -${discount.toLocaleString()} so'm\n`;\n            }\n            confirmMsg += `\n?? Jami: ${finalTotal.toLocaleString()} so'm`;"
new = "            if (promoResult.valid && discount > 0) {\n                confirmMsg += `? Chegirma: -${discount.toLocaleString()} so'm\n`;\n            }\n            if (deliveryMessage) {\n                confirmMsg += `?? ${deliveryMessage}\n`;\n            }\n            confirmMsg += `\n?? Jami: ${finalTotal.toLocaleString()} so'm`;"
if old not in text:
    raise SystemExit('promo block not found')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
print('delivery note added to confirm')
