import sqlite3


class Database:

    def __init__(self, db_name:str="database.db"):
        """
        Connects to database and be ready to call functions
        You also can pass your main table name if you want to use one table
        for many times

        Parameters
        ----------
        - db_name : str :
            Name or FilePath of your sqlite database.
            It creates if that db not found
            Defaut is "database.db"
        """
        try:
            self.db = sqlite3.connect(db_name)
        except sqlite3.Error:
            raise

    # >>> Functions to working with table >>>
    #_________________________________________

    def createtable(self, table_name:str, column_name:str) -> bool:
        """Creates a table inside connected database with some columns"""
        try:
            self.db.execute(f'CREATE TABLE {table_name}({column_name})')
            self.db.commit()
            return True
        except sqlite3.Error as Error:
            print(f"[SQLite Error][Creating Table] {Error}")
            return False

    def get_tables_name(self) -> list:
        """Return name of tables in your database"""
        try:
            self.db.row_factory = lambda cursor, row: row[0]
            cursor = self.db.cursor()
            return cursor.execute(
                "SELECT tbl_name FROM sqlite_master WHERE type='table'"
                ).fetchall()
        except sqlite3.Error as error:
            print(f"[SQLite Error][Getting tables name] {error}")
            return []

    def read_table(self, table_name:str=None, read_all:bool=False) -> list:
        """Read all/first column(s) of table"""
        if not read_all: # Gets only first column of database
            self.db.row_factory = lambda cursor, row: row[0]

        try:
            return self.db.execute(f'SELECT * FROM {table_name}').fetchall()
        except sqlite3.Error as error:
            print(f"[SQLite Error][Read Table] {error}")
            return []

    def delete_table(self, table_name:str) -> bool:
        """Delete table of database"""
        try:
            self.db.execute(f'DROP TABLE IF EXISTS {table_name}')
            self.db.commit()
            return True
        except sqlite3.Error as error:
            print(f"[SQLite Error][Delete Table] {error}")
            return False

    # >>> Functions to working with valus inside of table >>>
    #________________________________________________________


    def insert_value(self, table_name, column_name, value) -> bool:
        try:
            self.db.execute(f'INSERT INTO {table_name}({column_name}) VALUES ({value})')
            db.commit()
            return True
        except sqlite3.Error as Error:
            print(f"[SQLite Error][Insert Value] {Error}")
            return False

    def update_value(self, table_name, update_string, where) -> bool:
        try:
            self.db.execute(
                f"UPDATE {table_name} SET {update_string} WHERE {where}")
            self.db.commit()
            return True
        except sqlite3.Error as error:
            print(f"[SQLite Error][Update Value] {error}")
            return False

    def read_value(
        self, table_name:str, column_name:str, where:str=None,
        fetch_all:bool=True) -> str or list:

        cursor = self.db.cursor()
        base_string = f"""SELECT {column_name} FROM {table_name}"""

        try:
            if where is None:
                data = cursor.execute(base_string)
            else:
                data = cursor.execute(f"{base_string} WHERE {where}")

                return data.fetchall() if fetch_all else data.fetchone()
        except sqlite3.Error as error:
            print(f"[SQLite Error][Read Value] {error}")
            return [] if fetch_all else None

    def deletevalue(self, table_name, column_name, value_name) -> bool:
        """Delete value from table"""
        try:
            self.db.execute(f""" DELETE FROM {table_name}
                            WHERE {column_name}='{value_name}'""")
            self.db.commit()
            return True
        except sqlite3.Error as error:
            print(f"[SQLite Error][Delete Value] {error}")
            return False