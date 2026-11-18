class Server:

    def __init__(self, name:str):
        self.name = name
        self.duties = 'clear tables, mop the floor, take payment, serve customer'.split(',')

    def __str__(self):
        return f'My name is {self.name} and I am responsible for: {self.duties}'