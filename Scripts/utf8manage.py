# JUNESEOK BYUN @juneseokdev.me
import re
import regex

def cutKorean(x, n):
    if x == '.':
        return '0,0'
    print(x)
    p = regex.findall(r'\p{Hangul}', x)
    l = len(p)
    text = ''

    for i in range(0, n):
        text = text + p[i]

    return text
