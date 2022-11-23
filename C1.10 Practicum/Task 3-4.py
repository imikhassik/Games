class Client:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'

    def get_info(self):
        return f'{self.first_name} {self.last_name}, {self.city}'


client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Борис', 'Козявкин', 'Санкт-Петербург', 10)
client_3 = Client('Антон', 'Букахин', 'Казань', 1000)

client_list = [client_1, client_2, client_3]

for client in client_list:
    print(client.get_info())
