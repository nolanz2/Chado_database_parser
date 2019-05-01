#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector



def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')
    
    #use value of the chosen dropdown box selection as source of which database to connect to
   
    if form.getvalue('databases'):
        drop_term = form.getvalue('databases')

    conn = mysql.connector.connect(user='username', password='password', host='localhost', database=drop_term)
    cursor = conn.cursor()
    
    qry = """
	  SELECT f.uniquename, product.value, locn.fmin, locn.fmax
	    FROM feature f 
	    JOIN cvterm polypeptide ON f.type_id=polypeptide.cvterm_id 
	    JOIN featureprop product ON f.feature_id=product.feature_id 
	    JOIN cvterm productprop ON product.type_id=productprop.cvterm_id 
            JOIN featureloc locn ON f.feature_id = locn.feature_id
            JOIN feature src ON locn.srcfeature_id = src.feature_id
            JOIN cvterm srctype ON src.type_id = srctype.cvterm_id
	    JOIN organism org ON f.organism_id = org.organism_id
 	   WHERE product.value LIKE %s
    """
    cursor.execute(qry, ('%' + str(term) + '%', ))

    results = { 'match_count': 0, 'matches': list()}
    for (uniquename, value, fmin, fmax) in cursor:
        results['matches'].append({'locus_id': uniquename.decode('utf-8'), 'product': value.decode('utf-8'), 'fmin': fmin, 'fmax': fmax})


        results['match_count'] += 1

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()
