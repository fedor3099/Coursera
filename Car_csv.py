'''
Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице.

BaseCar

Car(BaseCar)

Truck(BaseCar)

SpecMachine(BaseCar)

У любого объекта есть обязательный атрибут car_type.
Он означает тип объекта и может принимать одно из значений: car, truck, spec_machine.
'''


import os
import csv


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.__body_whl = body_whl
        if self.__body_whl == "":
            self.body_length = self.body_width = self.body_height = float(0)
        else:
            self.body_length, self.body_width, self.body_height = map(float, self.__body_whl.split("x"))

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding='utf8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) == 0:
                continue
            elif row[0] == 'car':
                c = Car(row[0], row[1], row[3], row[5], row[2]);
                car_list.append(c)
            elif row[0] == 'truck':
                c = Truck(row[0], row[1], row[3], row[5], row[4])
                car_list.append(c)
            elif row[0] == 'spec_machine':
                c = SpecMachine(row[0], row[1], row[3], row[5], row[6])
                car_list.append(c)
    return car_list

