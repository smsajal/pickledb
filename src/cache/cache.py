from collections import OrderedDict
import src.interfaces.queryEngine as QueryEngine
from lru import LRU

cacheSize = 5
cache=LRU(cacheSize)

def cache_checkQuery(query):
    chunks1 = query.split('.')
    query_without_qe = chunks1[1]
    chunks2 = query_without_qe.split('(')
    if ((chunks2[0] == "tableInsert") or (chunks2[0] == "bulkInsertTable") or (chunks2[0] == "bulkInsertTableJSON")):
        # print("write")
        cacheWrite(query)
    else:
        # print("read")
        cacheRead(query)

def cacheRead(query):
    toReturn = ""
    # print("Query in cacheRead: ",query)
    # print("Query Eval in cacheRead: ", eval(query))
    if cache.has_key(query):
        # print(cache[query])
        toReturn = cache[query]
        print("hit")
    else:
        cache[query] = eval(query)
        toReturn = eval(query)
        print("miss")
    # print("Print Return in cacheRead", toReturn)
    return toReturn

def cacheWrite(query):
    # print("Query in cacheWrite: ", query)
    # print("Query Eval in cacheWrite: ", eval(query))
    eval(query)
    tableName = query.split("'")
    # print(tableName[1])
    for x in cache.keys():
        tableName_key = x.split("'")
        # print(tableName_key[1])
        if tableName_key[1] == tableName[1]:
            del cache[x]
            print("deleted", x)


def test():

    # for i in range(cacheSize):
    #     cache[i] = str(i)
    # print(cache.items())
    cache_checkQuery("QueryEngine.median('tablex', 'dbx','birthYear')")
    cache_checkQuery("QueryEngine.mean('tablex', 'dbx','birthYear')")
    cache_checkQuery("QueryEngine.mean('tablex', 'dbx','birthYear')")
    cache_checkQuery("QueryEngine.bulkInsertTableJSON('tablex','dbx','nconst', '/Users/avimitachatterjee/Documents/PSU/CourseWork/541 - DBMS/Project/JSONTest.json')")
    cache_checkQuery("QueryEngine.mean('imdb_names', 'imdb_kaggle_small','height')")
    cache_checkQuery("QueryEngine.sum('title_principals', 'imdb_kaggle_small','ordering')")
    cache_checkQuery("QueryEngine.median('title_principals', 'imdb_kaggle_small','ordering')")
    cache_checkQuery("QueryEngine.median('imdb_ratings', 'imdb_kaggle_small','total_votes')")
    cache_checkQuery("QueryEngine.mean('title_principals', 'imdb_kaggle_small','ordering')")
    cache_checkQuery("QueryEngine.mean('imdb_names', 'imdb_kaggle_small','height')")
    cache_checkQuery("QueryEngine.mean('imdb_names', 'imdb_kaggle_small','height')")
    cache_checkQuery("QueryEngine.median('title_principals', 'imdb_kaggle_small','ordering')")

if __name__ == "__main__":
    test()