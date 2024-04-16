from pymysql import cursors, connect

connection = connect(host='localhost',
                     user='root',
                     password='Aaibaba',
                     database='PRACTISE',
                     port=3306,
                     cursorclass=cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # sql = 'SHOW DATABASES'
        sql = 'SELECT * FROM PRACTISE.Random' # this is how we read the data from database
        # sql = 'INSERT INTO `Random` (`int_data`, `str_data`) values (4, "Arnav")' this is
        cursor.execute(sql)
        result = cursor.fetchall()  # it will return a list of dictionaries
        # cursor.fetchone() it will return a dictionary
        print(result)

    connection.commit()  # with commit it will update the changes
    breakpoint()
