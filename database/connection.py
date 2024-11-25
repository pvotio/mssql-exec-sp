import logging
import struct

import pyodbc
from azure.identity import DefaultAzureCredential
from decouple import config

logger = logging.getLogger(__name__)


def pyodbc_attrs(access_token: str) -> dict:
    SQL_COPT_SS_ACCESS_TOKEN = 1256
    token_bytes = bytes(access_token, "utf-8")
    exp_token = b""
    for i in token_bytes:
        exp_token += bytes({i}) + bytes(1)
    return {SQL_COPT_SS_ACCESS_TOKEN: struct.pack("=i", len(exp_token)) + exp_token}


class MSSQLDatabase(object):
    ad_login = config("MSSQL_AD_LOGIN", cast=bool, default=False)
    server = config("MSSQL_SERVER", cast=str)
    database = config("MSSQL_DATABASE", cast=str)

    if not ad_login:
        username = config("MSSQL_USERNAME", cast=str)
        password = config("MSSQL_PASSWORD", cast=str)
        connection_url = (
            "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
            + server
            + ";DATABASE="
            + database
            + ";UID="
            + username
            + ";PWD="
            + password
        )
    else:
        connection_url = (
            "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
            + server
            + ";DATABASE="
            + database
            + ";Encrypt=yes"
        )

    def __init__(self):
        kwargs = {}
        if self.ad_login:
            token = self.fecth_token()
            kwargs["attrs_before"] = pyodbc_attrs(token)

        self.connection = pyodbc.connect(self.connection_url, **kwargs)

    def execute(self, sp_name):
        query = f"EXECUTE {sp_name}"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            cursor.commit()
            cursor.close()
            return True
        except Exception as e:
            logger.error(e)
            raise

    def fecth_token(self):
        credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)
        token = credential.get_token("https://database.windows.net/.default").token
        return token
