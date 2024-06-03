import pymysql
import toml
from pymysql import connect  # cursors
import yaml


def get_toml_conn():
    try:
        with open('data_access_layer/settings/secrets.toml') as fp:
            toml_config = toml.load(fp)
            toml_db_config = toml_config.get('mysqldb')
            t_connection = connect(**toml_db_config)
            return t_connection
    except pymysql.Error as ex:
        print(f"[ ERROR ] connection cannot successful - {ex}")


def get_yaml_conn():
    try:
        with open("data_access_layer/settings/secrets.yaml") as fp:
            yaml_config = yaml.load(fp, Loader=yaml.FullLoader)
            y_connection = connect(**yaml_config)
            return y_connection
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
#         print(f"[ ERROR ] connection cannot successful - {ex}")

if __name__ == "__main__":
    toml_conn = get_toml_conn()
    yaml_conn = get_yaml_conn()
    breakpoint()

