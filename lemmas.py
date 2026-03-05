from collections import defaultdict
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

tokens_file = "tokens.txt"
output_file = "lemmas.txt"

lemma_groups = defaultdict(set)

# 1. читаем токены
with open(tokens_file, "r", encoding="utf-8") as f:
    tokens = [line.strip() for line in f if line.strip()]

# 2. группируем по леммам
for token in tokens:
    token = token.replace('ё', 'е')
    parsed = morph.parse(token)[0]
    lemma = parsed.normal_form
    lemma = lemma.replace('ё', 'е')
    lemma_groups[lemma].add(token)

# 3. запись результата
with open(output_file, "w", encoding="utf-8") as f:
    for lemma in sorted(lemma_groups):
        tokens_list = " ".join(sorted(lemma_groups[lemma]))
        f.write(f"{lemma} {tokens_list}\n")

print(f"Создан файл {output_file} с {len(lemma_groups)} леммами.")