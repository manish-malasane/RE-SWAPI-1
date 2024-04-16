import pymysql
import toml
from pymysql import connect, cursors


def make_connection():
    try:
        connection = connect(host='localhost',
                             user='root',
                             password='Aaibaba',
                             port=3306,
                             database='PRACTISE',
                             cursorclass=cursors.DictCursor)
        return connection
    except pymysql.Error as ex:
        print(f"[ ERROR ] connection cannot successfull - {ex}")


def get_toml_conn():
    with open('data_access_layer/settings/secrets.toml') as fp:
        config = toml.load(fp)
        print(config)


if __name__ == "__main__":
    conn = make_connection()
    get_toml_conn()
    breakpoint()
