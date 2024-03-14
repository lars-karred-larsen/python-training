'''
Created on Mar 11, 2024

@author: student
'''
def test_database_connection(db_connection):
    assert db_connection is not None
    
    # Performa a simple query to verify the connection
    cursor = db_connection.cursor()
    cursor.execute( "SELECT 1")
    result = cursor.fetchone()
    # Check if the query result is as expected
    assert result == (1,)