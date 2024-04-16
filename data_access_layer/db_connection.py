import pymysql
import toml
from pymysql import connect, cursors


def get_toml_conn():
    try:
        with open('data_access_layer/settings/secrets.toml') as fp:
            config = toml.load(fp)
            db_config = config.get('mysqldb')
            connection = connect(**db_config)
            return connection
    except pymysql.Error as ex:
        print(f"[ ERROR ] connection cannot successful - {ex}")


# def make_connection():
#     try:
#         connection = connect(host='localhost',
#                              user='root',
#                              password='Aaibaba',
#                              port=3306,
#                              database='PRACTISE',
#                              cursorclass=cursors.DictCursor)
#         return connection
#     except pymysql.Error as ex:
#         print(f"[ ERROR ] connection cannot successfull - {ex}")

if __name__ == "__main__":
    get_toml_conn()
    breakpoint()
