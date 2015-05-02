__author__ = 'miller'
import nytquery
from datetime import datetime
import json
import re, math
from collections import Counter


WORD = re.compile(r'\w+')


def strToJson(s):
    return json.load(s)


def strToDate(s):
    return datetime.strptime(s, '%Y-%m-%d').date()


def queryIndex(index, n, key):
    s = nytquery.query(index, n, key)
    ret = []
    for l in s.split('\n'):
        x = l.split('\t')
        try:
            ret.append({'id': x[0], 'score': float(x[1])})
        except IndexError:
            print("Empty Search!")
    return ret


def queryResult(n, key, other, hw=0.8):
    result = {}
    alpha = [hw, 1 - hw]
    for i in range(0, 2):
        for x in queryIndex(i, n, key):
            result[x['id']] = {'score': x['score'] * alpha[i]}
        for x in other:
            if x != "":
                for z in queryIndex(i, n, key + " " + x):
                    if z['id'] in result:
                        result[z['id']]['score'] += z['score'] * alpha[i]
                    else:
                        result[z['id']] = {'score': z['score'] * alpha[i]}
    return result


def get_cosine(s1, s2):
    def text_to_vector(text):
        words = WORD.findall(text.lower())
        return Counter(words)

    vec1 = text_to_vector(s1)
    vec2 = text_to_vector(s2)
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


