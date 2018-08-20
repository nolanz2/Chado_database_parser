#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector
import sys

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('term')
        
    conn = mysql.connector.connect(user='hopkins', password='fakepass', host='localhost', database='biotest')
    cursor = conn.cursor()
    
    qry = """
          SELECT locus_id, product
            FROM genes
           WHERE product LIKE %s
	   LIMIT 0,5
    """
    cursor.execute(qry, ('%' + str(term) + '%', ))

    results = []
    for (locus_id, product) in cursor:
        results.append({'value': product, 'label': product})

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()
