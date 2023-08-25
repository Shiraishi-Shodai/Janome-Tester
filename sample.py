from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *

text = "今日は美しい花を見に公園に行きました。"

t = Tokenizer()
for token in t.tokenize(text):
    print(token)
