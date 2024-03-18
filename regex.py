import re

txt = "there will be no explanation, there will just be reputation"

regex = r'there\w*\s*reputation'

match = re.match(regex, txt)

if match:
    print("match")
    print(match)
else:
    print("no match")

txt = "oi! teu pai tem boi? Foi o que pensei."

regex = r'oi'

ans = re.findall(regex, txt)

if ans:
    print(f"match: {len(ans)} ocurrences found")
    print(ans)
else:
    print("no match")

txt = "O rato roeu a roupa do rei de roma. Que rato danado!"

regex = r'\br[a-z]+\b'

ans = re.search(regex, txt)

if ans:
    print(ans)
    print(f'inicio: {ans.start()}')
    print(f'fim: {ans.end()}')
    print(f'span: {ans.span()}')
    print(f'grupo: {ans.group()}')

else:
    print("no match")

for match in re.finditer(regex, txt):
    print(f"match: {match.span()}")
    print(f"match: {match.group()}")
    print(f"match: {match.start()}")
    print(f"match: {match.end()}")
    print()

txt = "Eu gosto de sorvete de chocolate; meu pai, de creme; meu irmão, de morango"
split = re.split(";", txt)

for i in split:
    print(f'[{i}]')

for i, split_i in enumerate(split):
    print(f'split {i} -> {split_i}')

txt = "Quando chover, busque pelo arco-íris. Quando escurecer, busque pelas estrelas."

pattern = r"\b[A-Z]?[a-z]+r\b"
replacement = "coisar"

sub = re.sub(pattern, replacement, txt)

print(sub)
