'''
Created on Mar 12, 2024

@author: student
'''
import pytest
import psycopg2

# Fixture to provide a database connection
@pytest.fixture(scope="module")
def setup():
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
    
    yield connection # All before yield is considered "setup" all after "tear-down"
    
    # Close the database connection
    connection.close()
    
def test_database_connection(setup):
    assert setup is not None
    
    # Perform a simple query to verify the connection
    cursor = setup.cursor()
    cursor.execute( "SELECT 1")
    result = cursor.fetchone()
    # Check if the query result is as expected
    assert result == (1,)
