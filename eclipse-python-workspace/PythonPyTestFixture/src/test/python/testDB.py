'''
Created on Mar 11, 2024

@author: student
'''
import pytest

import psycopg2


# Fixture to provide a database connection
@pytest.fixture(scope="module")
def db_connection():
    #Replace these with your actual database credentials
    db_host = "127.0.0.1"
    db_name = "testing"
    db_user = "student"
    db_password = "student"
    
    # Establish a connection to the database
    connection = psycopg2.connect(
        host = db_host,
        database = db_name,
        user = db_user,
        password = db_password
    )
    
    yield connection
    
    # Close the database connection
    connection.close()
    
# Test function to check if the database connection is established
def test_database_connection(db_connection):
    assert db_connection is not None
    
    # Performa a simple query to verify the connection
    cursor = db_connection.cursor()
    cursor.execute( "SELECT 1")
    result = cursor.fetchone()
    # Check if the query result is as expected
    assert result == (1,)
        
