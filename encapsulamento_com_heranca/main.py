class DatabaseConnect:
    def __init__(self) -> None:
        self.__database = "postgres"
        self._conn = "//conection_string"
        self.user = "Ana Paula"

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None:
        print("Connection OK")

class Repository(DatabaseConnect):
    def __init__(self) -> None:
        super().__init__()
        #print(self.user)
        #print(self._conn)

    def select(self) -> None:
        self._testing_connection()
        print(f"Conexão para {self._conn}")
        print("SELECT * FROM table;")

repo = Repository()

repo.select()