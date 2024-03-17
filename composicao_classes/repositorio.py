from sql_actions.insert import Insert
from sql_actions.select import Select

class Repositorio:
    def __init__(self):
        self.__insert = Insert() # obj na classe Repositorio
        self.__select = Select()

    def select_by_id(self):
        self.__select.select_one()