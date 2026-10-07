import re 

def normalize(text, casefold: bool = True, yo2e:bool = True):
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.casefold().replace("ё", "е").strip()
    res_text = " ".join(text.split())
    return res_text

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка", yo2e=True))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))


def tokenize(text):
    text = normalize(text)
    new_text = re.findall(r"\w+(?:-\w+)*", text)
    return new_text

print(tokenize("ПрИвЕт\nМИр\t"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

def count_freq(tokens):
    res = {}
    for w in tokens:
        res[w] = res.get(w, 0) + 1
    return res    

print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))

test1 = count_freq(["a","b","a","c","b","a"])
test2 = {"aa":2,"bb":2,"cc":1}

def top_n(freq, n):
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))[:n]

print(top_n(test1, 2))
print(top_n(test2, 2))
