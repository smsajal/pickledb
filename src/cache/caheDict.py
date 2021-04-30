import src.interfaces.queryEngine as QueryEngine

cacheSize = 100
cache = {}

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
    # print("Query in cacheRead: ",query)
    # print("Query Eval in cacheRead: ", eval(query))
    if query in cache.keys():
        # print(cache[query])
        toReturn = cache[query]
        # print("hit")
    else:
        if len(cache) == cacheSize:
            list_keys = list(cache.keys())
            first_key = list_keys[0]
            cache.pop(first_key)
            toReturn = eval(query)
            cache.update({query: toReturn})
            # print("miss1")
        else:
            toReturn = eval(query)
            cache.update( {query : toReturn} )
            # print("miss2")
    # print("Print Return in cacheRead", toReturn)
    return toReturn

def cacheWrite(query):
    # print("Query in cacheWrite: ", query)
    # print("Query Eval in cacheWrite: ", eval(query))
    eval(query)
    tableName = query.split('"')
    # print(tableName[1])
    for x in list(cache.keys()):
        tableName_key = x.split("'")
        # print(tableName_key[1])
        if tableName_key[1] == tableName[1]:
            # print("deleted", x)
            cache.pop(x)

def printCache():
    print(cache)


def test():


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

    printCache()
    # dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    # print(dict)
    # print(len(dict))
    #
    # if 'Name' in dict.keys():
    #     print(dict['Name'])
    # print(dict.get('Name'))
    #
    # dict.update( {'Germany' : 49} )
    # print(len(dict))
    # print(list(dict.keys())[0])
    # dict.pop(list(dict.keys())[0])
    # print(len(dict))
    #
    # print(dict)

    # dict.clear()
    # print(dict)

    # for x in list(dict.keys()):
    #     print(x)




if __name__ == "__main__":
    test()