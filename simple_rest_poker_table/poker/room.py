from simple_rest_poker_table.poker.table import Table

class Room:
    def __init__(self):
        self.tables = []
    
    def add_table(self, table: Table):
        self.tables.append(table)