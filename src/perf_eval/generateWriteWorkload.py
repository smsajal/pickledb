import random
import string
import json
from src.storage.table import Table
from src.storage.tempResult import TempResult
from src.interfaces import queryEngine

letters = string.ascii_lowercase
numbers = string.digits

#all primary key values should be greater than nm0023000 (nm0022697)
def generateMovies(primaryKey):
    query = "tableInsert(movies, {'imdb_title_id': '"
    #randomString = ''.join(random.choice(numbers) for i in range(4))
    query = query + primaryKey + "', 'title': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString +  "', 'original_title': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "', 'year': '1"
    randomString = ''.join(random.choice(numbers) for i in range(3))
    query = query + randomString + "', 'date_published': '1953-08-10', 'genre': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "', 'duration': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "', 'country': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "', 'language': 'English', 'director': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'writer': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'production_company': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'actors': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + ","
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'description': '"
    randomString = ''.join(random.choice(letters) for i in range(10))
    query = query + randomString + "', 'avg_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'votes': '"
    randomString = ''.join(random.choice(numbers) for i in range(4))
    query = query + randomString + "', 'budget': '', 'usa_gross_income': '', 'worlwide_gross_income': '', 'metascore': '', 'reviews_from_users': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "', 'reviews_from_critics': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "'})"
    print(query)
    return query


#all primary key values greater than tt0060000 (tt0052961)
def generateNames(primaryKey):
    query = "tableInsert(names, {'imdb_name_id': '"
    query = query + primaryKey + "', 'name': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "', 'birth_name': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "', 'height': '1"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "', 'bio': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "', 'birth_details': '"
    randomString = ''.join(random.choice(letters) for i in range(10))
    query = query + randomString + "', 'date_of_birth': '1899-05-10', 'place_of_birth': '"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "', 'death_details': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'date_of_death': '1987-06-22', 'place_of_death': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'reason_of_death': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'spouses_string': '"
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + ","
    randomString = ''.join(random.choice(letters) for i in range(6))
    query = query + randomString + "', 'spouses': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'divorces': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'spouses_with_children': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'children': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "'})"
    print(query)
    return query

#all primary key values greater than tt0053000 (tt0052961)
def generateRatings(primaryKey):
    voteCount = 0
    query = "tableInsert(ratings, {'imdb_title_id': '"
    query = query + primaryKey + "', 'weighted_average_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'total_votes': '"
    randomString = ''.join(random.choice(numbers) for i in range(3))
    voteCount = int(randomString)
    query = query + randomString + "', 'mean_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'median_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'votes_10': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_9': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_8': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_7': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_6': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_5': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_4': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_3': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_2': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    voteCount -= int(randomString)
    query = query + randomString + "', 'votes_1': '"
    randomString = str(voteCount)
    query = query + randomString + "', 'allgenders_0age_avg_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'allgenders_0age_votes': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'allgenders_18age_avg_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'allgenders_18age_votes': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'allgenders_30age_avg_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'allgenders_30age_votes': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'allgenders_45age_avg_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'allgenders_45age_votes': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'males_allages_avg_vote': '"
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'males_allages_votes': '"
    randomString = ''.join(random.choice(numbers) for i in range(2))
    query = query + randomString + "."
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "', 'males_0age_avg_vote': '7.0', 'males_0age_votes': '1.0', 'males_18age_avg_vote': '5.9', 'males_18age_votes': '24.0', 'males_30age_avg_vote': '5.6', 'males_30age_votes': '36.0', 'males_45age_avg_vote': '6.7', 'males_45age_votes': '31.0', 'females_allages_avg_vote': '6.0', 'females_allages_votes': '35.0', 'females_0age_avg_vote': '7.3', 'females_0age_votes': '3.0', 'females_18age_avg_vote': '5.9', 'females_18age_votes': '14.0', 'females_30age_avg_vote': '5.7', 'females_30age_votes': '13.0', 'females_45age_avg_vote': '4.5', 'females_45age_votes': '4.0', 'top1000_voters_rating': '5.7', 'top1000_voters_votes': '34.0', 'us_voters_rating': '6.4', 'us_voters_votes': '51.0', 'non_us_voters_rating': '6.0', 'non_us_voters_votes': '70.0'})"
    print(query)
    return query

#all primary key values greater than  (tt0052961)
def generateTitle_principals():
    query = "queryEngine.tableInsert(title_principals, \"{\"imdb_title_id\": \"tt00"
    randomString = ''.join(random.choice(numbers) for i in range(5))
    query = query + randomString + "\", \"ordering\": \""
    randomString = ''.join(random.choice(numbers) for i in range(1))
    query = query + randomString + "\", \"imdb_name_id\": \"nm00"
    randomString = ''.join(random.choice(numbers) for i in range(5))
    query = query + randomString + "\", \"category\": \""
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "\", \"job\": \"\", \"characters\": \"[\'"
    randomString = ''.join(random.choice(letters) for i in range(5))
    query = query + randomString + "\']\"}\")"
    print(query)
    return query


if __name__ == '__main__':
    q = generateMovies("tt0060001")
    print(q)
    q = generateNames("nm230011")
    print(q)
    #generate rating could check if entry present in movies table
    q = generateRatings("tt0063001")
    print(q)
    q = generateTitle_principals()
    print(q, "\n")
    title_principals = Table(tableName="title_principals", dbName="imdb_kaggle_small").vanillaSelect()
    # ret = eval("queryEngine.tableInsert(title_principals, \"{\\\"imdb_title_id\\\": \\\"tt0063852\\\", \\\"ordering\\\": \\\"2\\\", \\\"imdb_name_id\\\": \\\"nm0028414\\\", \\\"category\\\": \\\"hllnf\\\", \\\"job\\\": \\\"\\\", \\\"characters\\\": \\\"[\\\\\\\"xeczz\\\\\\\"]\\\"}\") ")
    # print(ret)
    x=json.loads("{\"imdb_title_id\": \"tt0018113\", \"ordering\": \"1\", \"imdb_name_id\": \"nm0841797\", \"category\": \"actress\", \"job\": \"\", \"characters\": \"[\\\"Sunya Ashling\\\"]\"}")
    queryEngine.tableInsert(
        title_principals,x )