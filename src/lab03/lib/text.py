def normalize(text, casefold: bool = True, yo2e:bool = True):
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.casefold().replace("ё", "е").strip()
    res_text = " ".join(text.split())
    return res_text

import re 
def tokenize(text):
    text = normalize(text)
    new_text = re.findall(r"\w+(?:-\w+)*", text)
    return new_text


def count_freq(tokens):
    res = {}
    for w in tokens:
        res[w] = res.get(w, 0) + 1
    return res  


def top_n(freq, n):
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))[:n]


