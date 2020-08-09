#!/usr/bin/env python3

#==============================================================================
# Importing necessary libraries

import pymysql.cursors
import mysql.connector
import pymysql

#==============================================================================
# Importing necessary modules (data for database and configuration details)
# dbtable: the data to be imported
# connection_config_dict: dictionary that contains username, password and connection details
#==============================================================================

connection = pymysql.connect(**connection_config_dict)
cursor = connection.cursor()
create_query = (
    "CREATE TABLE yourdb.yourtable ("
    "  accession CHAR(20) DEFAULT 'N/A' NOT NULL,"
    "  cds_joins TEXT NOT NULL,"
    "  gene_size INT UNSIGNED,"
    "  cds_info CHAR(20) DEFAULT 'N/A',"
    "  dna_seq MEDIUMTEXT NOT NULL,"
    "  protein_name TEXT,"
    "  protein_seq MEDIUMTEXT NOT NULL,"
    "  location TEXT NOT NULL,"
    "  gene_name TEXT,"
    "  PRIMARY KEY (accession)"
    ") ENGINE=InnoDB")

drop_query = ("DROP TABLE yourdb.yourtable")
try:
    cursor.execute(create_query)
except pymysql.InternalError as e:
    response = input('Table already exists in the database, do you want to drop and create it again? \n You will lose your data \n y/n: ')
    if response.lower() == 'y':
        cursor.execute(drop_query)
        print('The table is dropped')
        cursor.execute(create_query)
        print('The table is created again')
    else:
        exit()
else:
    print('Table created successfully')
connection.commit()
connection.close()

# Populating the database
connection = pymysql.connect(**connection_config_dict)
cursor = connection.cursor()
fill_yourtable = "INSERT INTO yourdb.yourtable VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cursor = connection.cursor()
cursor.executemany(fill_yourtable, dbtable)
connection.commit()
connection.close()

#==============================================================================
