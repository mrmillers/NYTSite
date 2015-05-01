__author__ = 'miller'
import nytquery
from datetime import datetime
import json;


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
    alpha = [hw, 1-hw]
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
