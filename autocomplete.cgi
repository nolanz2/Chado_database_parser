#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector
import sys


def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('term')
    
    # Wouldn't get value of dropdown because because it's value seems to be null before from is submitted
    # drop_term = form.getvalue('databases')
    # print(drop_term)

    conn = mysql.connector.connect(user='username', password='password', host='localhost', database='database')
    cursor = conn.cursor()
   

    
    qry = """
	  SELECT f.uniquename, product.value
	    FROM feature f 
	    JOIN cvterm polypeptide ON f.type_id=polypeptide.cvterm_id 
	    JOIN featureprop product ON f.feature_id=product.feature_id 
	    JOIN cvterm productprop ON product.type_id=productprop.cvterm_id 
 	   WHERE value LIKE %s
	   LIMIT 0,5
    """
    cursor.execute(qry, ('%' + str(term) + '%', ))

    results = []
    for (uniquename, value) in cursor:
        results.append({'value': uniquename.decode("utf-8"), 'label': value.decode("utf-8")})

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()
