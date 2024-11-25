import logging

from decouple import config

from database import connection

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)
SP_NAME = config("SP_NAME", cast=str)


def main(sp_name):
    mssql = connection.MSSQLDatabase()
    return mssql.execute(sp_name)


if __name__ == "__main__":
    logger.info(f"Executing {SP_NAME}...")
    main(SP_NAME)
    logger.info(f"{SP_NAME} executed.")
