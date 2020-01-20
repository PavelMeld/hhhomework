#!/usr/bin/python
# -*- coding: utf-8 -*-
class Car:
    maker = "";
    model = "";

    def __init__(self, maker, model):
        self.maker = maker;
        self.model = model;

    def __repr__(self):
        return "{} {}".format(self.maker, self.model);


class Garage:
    cars = [];
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража

    def __init__(self, cars = []):
        self.cars = cars;

    def __iter__(self):
        return iter(self.cars);

    def add(self, car):
        self.cars.append(car);

    def delete(self, index):
        self.cars.pop(index);


if __name__ == "__main__":
    a = Car("Toyota", "Corolla");
    b = Car("Ford", "Focus");
    c = Car("Smart", "ForTwo");
    garage = Garage([a, b]);
    garage.add(c);
    garage.delete(1);
    for car in garage :
        print(car);
        for car2 in garage :
            print("   {}".format(car2));
