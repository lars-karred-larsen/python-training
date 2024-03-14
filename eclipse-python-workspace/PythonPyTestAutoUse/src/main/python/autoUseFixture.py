'''
Created on Mar 11, 2024

@author: student
'''
import pytest
import psycopg2

# Fixture to provide a database connection
#@pytest.fixture(scope="module")
@pytest.fixture(scope="module", autouse=True)
def db_data():
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
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Execute a SELECT * query
    cursor.execute("SELECT * FROM example")
    
    # Fetch the result
    result = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Yield the query results to the test functions
    return result

# Test function to check if the database connection is established and SELECT * query executed
def test_database_data(db_data):
    assert db_data is not None
    
    # Check if the query result is not empty
    assert len(db_data) > 0
    
    # Perform additional assertions on the query results, if needed
    for row in db_data:
        # Perform assertions on each row of the query results
        assert isinstance(row, tuple) # Example assertion, ensuring each row is a tuple
    
 
