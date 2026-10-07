
import sys

from lib.text import tokenize, count_freq, top_n

text = sys.stdin.read()

tokens = tokenize(text)
freq = count_freq(tokens)
top = top_n(freq, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

for word, count in top:
    print(f"{word}:{count}")