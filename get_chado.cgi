#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

print("Content-Type: application/json\n\n")

chado_list = list()
conn = mysql.connector.connect(user='ncligro1', password='Fuckme44', host='localhost', buffered=True)
cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)
for (databases) in cursor:
    chado_list.append({'chado_list': databases[0]})

for x in chado_list:
    if 'chado' not in x:
        chado_list.remove(x)

print(json.dumps(chado_list))

