import re

txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz."

regex = r'\b\w+\b'

ans = re.findall(regex, txt)

print(f"{len(ans)} palavras")
print(ans)
