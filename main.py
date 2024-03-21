# Завдання 1
# Створіть систему управління замовленнями
# готелю. Кожне замовлення має містити інформацію
# про клієнта, тип кімнати, кількість днів проживання та
# вартість. Реалізуйте методи для додавання замовлення,
# зміни типу кімнати та кількості днів, а також
# видалення замовлення. Використайте інкапсуляцію для
# захисту вартості від неправильних змін.
class Order:
    def __init__(self, customer_information, room_type, stay_duration, cost_per_day):
        self.__customer_information = customer_information
        self.__room_type = room_type
        self.__stay_duration = stay_duration
        self.__cost_per_day = cost_per_day
        self.__cost = self.__stay_duration * self.__cost_per_day

    def get_customer_information(self):
        return self.__customer_information

    def set_customer_information(self, customer_information):
        self.__customer_information = customer_information

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, new_room_type):
        if new_room_type in room_types:
            self.__room_type = new_room_type
            self.__cost = self.__stay_duration * self.__cost_per_day
        else:
            print("Виникла помилка, неправильний ввід даних")

    def get_stay_duration(self):
        return self.__stay_duration

    def set_stay_duration(self, new_stay_duration):
        if new_stay_duration in stay_durationss:
            self.__stay_duration = new_stay_duration
            self.__cost = self.__stay_duration * self.__cost_per_day
        else:
            print("Виникла помилка, неправильний ввід даних")

    def get_cost(self):
        return self.__cost

    def delete(self):
        print("Замовлення видалене :(")
        pass
        self.__cost = 0
        self.__customer_information = "Видалено"
        self.__room_type = 0
        self.__stay_duration = 0


room_types = [150, 200, 300]
stay_durationss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

order1 = Order("Іван", 150, 4, 150)
print("Початкове замовлення: ", order1.get_cost())
order1.set_stay_duration(8)
print("Замовлення після зміни кількості днів проживання: ", order1.get_cost())
order1.set_room_type(150)
print("Замовлення після зміни типу кімнати: ", order1.get_room_type())
order1.delete()
print("Вартість після видалення замовлення: ", order1.get_cost())

# Завдання 2
# Розробіть систему управління замовленнями таксі.
# Кожне замовлення має містити інформацію про
# клієнта, адресу, тип автомобіля та вартість. Реалізуйте
# методи для додавання нових замовлень, зміни адреси та
# типу автомобіля, а також видалення замовлення.
# Використайте інкапсуляцію для захисту вартості від
# неправильних змін.
class TaxiOrder:
    def __init__(self, client, address, car_type, cost):
        self.__client = client
        self.__address = address
        self.__car_type = car_type
        self.__cost = cost

    def get_client(self):
        return self.__client

    def set_client(self, client):
        self.__client = client

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_car_type(self):
        return self.__car_type

    def set_car_type(self, car_type):
        self.__car_type = car_type

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def delete(self):
        print("Замовлення видалено.")
        self.__client = "Видалено"
        self.__address = "Видалено"
        self.__car_type = "Видалено"
        self.__cost = 0

order1 = TaxiOrder("Іван", "Спортивна площа 1а", "Стандарт", 250)
print("Початкове замовлення: ", order1.get_cost())

order1.set_car_type("Бізнес")
print("Замовлення після зміни типу поїздки: ", order1.get_car_type())

order1.set_address("Поштова площа, 3")
print("Замовлення після зміни адреси: ", order1.get_address())

order1.delete()
print("Замовлення після видалення: ", order1.get_cost())








