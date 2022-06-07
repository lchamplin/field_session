##
# Program:      queryTestDriver
# Client:       ICR
# Team:         aMALGomation
# Author:       Graham Stookey
# Date:         06/06/2022
# Description:  Program reads in queries one at time, queries the instance of the neo4j database, 
#               measures query response time, and then finally, outputs time results to a .txt file

from dataclasses import replace
from Neo4jConnection import Neo4jConnection
from neo4j import GraphDatabase
import pandas as pd
import os
import time

localConnection = Neo4jConnection(uri="bolt://localhost:11010", user="gstookey", pwd="@Collin0820")
driver = GraphDatabase.driver('bolt://localhost:11010', auth=('gstookey', '@Collin0820'))
path = "/home/gstookey/ICR/fieldSession/app-python/api/neo4jDB_demo/data"

os.chdir(path) 

def get_query_from_file(file_path):
    with open(file_path, 'r') as queryFile:
        query = ""

        for line in queryFile:
            query += line.strip() + "\n"
    
    return query

def query_DB(query, query_times):

    n_repeats = 100

    with driver.session() as session:
        total_time = 0
        for _ in range(n_repeats):
            with session.begin_transaction() as t:
                start = time.time()
                t.run(query)
                end = time.time()
                total_time += end - start

    avg_time = total_time*1000 / n_repeats
    print('Average execution time:', avg_time, 'ms')
    query_times.append(avg_time)

counter = 0
queryNums = []
queries = []
queryTimes = []
for file in os.listdir():
    if file.endswith(".cypher"):
        file_path = f"{path}/{file}"
        query = get_query_from_file(file_path)
        print("Query", counter, ":\n",query, "\n")
        queries.append(query)
        query_DB(query, queryTimes)
        counter += 1
        queryNums.append(counter)

queryTimesDict = {
    'Query Number' : queryNums,
    'Query' : queries,
    'Avg. Query Response Time' : queryTimes
}

df = pd.DataFrame(queryTimesDict)
print(df.head())
  




# dtf_data = DataFrame([dict(_) for _ in localConnection.query(query)])
# dtf_data.head
