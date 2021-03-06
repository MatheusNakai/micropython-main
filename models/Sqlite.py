
class Sqlite(object):

    def __init__(self):
        self.db = None
        self.create_connection()


    def close_connection(self):
        self.db.close()

    def execute_query(self, query: str):
        cursor = self.db.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as err:
            print(err)
            return None

    def custom_search(self,dictionary: dict):
        table = dictionary["table"]
        column = dictionary["column"]
        where = dictionary["where"]
        result = self.execute_query(f"SELECT {column} FROM {table} WHERE {where}")
        if result is not None:
            for row in result:
                print(row)
            return result
        else:
            return None

    def insert_one(self,dictionary: dict):
        table = dictionary.pop("table")
        keys = ""
        values = ""
        for key, value in dictionary.items():
            keys += f"{key},"
            values += f"'{value}',"
        keys = keys[:-1]
        values = values[:-1]
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        self.execute_query(query)

    def insert_multiples(self,list_of_dict: list):
        for dicti in list_of_dict:
            self.insert_one(dicti)

    def update(self, dictionary: dict):
        id = dictionary["id"]
        table = dictionary.pop("table")
        query = f"UPDATE {table} SET "
        for key, value in dictionary.items():
            query += f"{key}='{value}',"
        query = query[:-1]
        query += f" WHERE id={id}"
        self.execute_query(query)
        self.db.commit()

    def delete(self,dictionary: dict):
        table = dictionary["table"]
        condition = dictionary["condition"]
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)
        self.db.commit()
    
    def get_one(self, dictionary: dict):
        result = self.custom_search(dictionary)
        if result is not None:
            return result[0]

    def get_multiple(self, dictionary: dict):
        list_Of_Dictionary = []
        result = self.custom_search(dictionary)
        if result is not None:
            for row in result:
                list_Of_Dictionary.append(row)
                self.close_connection()
            return list_Of_Dictionary
        else:
            print("tabela vazia")
    
    def create_table(self, dictionary: dict):
        table = dictionary.pop("table")
        keys = ""
        for key, value in dictionary.items():
            keys += f"{key} TEXT,"
            print(key)
        keys =keys[:-1]
        query = f"CREATE TABLE {table} ({keys});"
        print(query)
        self.execute_query(query)
        self.db.commit()


sqlite= Sqlite()
a={
    "table":"test",
    "a":"a",
    "b":1,
    "c":"2"
}
