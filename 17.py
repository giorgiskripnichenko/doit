


# ----------------- დავალება 17 -----------------

# 1. შექმენით პითონის კლასი Car, ატრიბუტებით ბრენდით, მოდელით და წლით. ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.

# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car class-ს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(),
    #  რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".

# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. 

# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.


class Car:
    number_of_cars_counter = 0
    def __init__(self, mark, model, year):
        Car.number_of_cars_counter += 1
        self.mark = mark
        self.model = model
        self.year = year
    def car_info(self):
        print(self.mark,self.model,self.year)
    def age_of_car(self):
        print(2024-self.year)
    def total_cars(self):
        print('total_cars =',self.number_of_cars_counter)

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_life):
        super().__init__(make,model,year)
        self.battery_life_ = battery_life
    def battery_life(self):
        print(f'ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life_} საათი')
        
nissan = Car('nissan','juke',1991)
nissan.car_info()
nissan.age_of_car()

prius = ElectricCar('toyota','prius',2012,20)
prius.battery_life()

mercedes = Car('marka','modeli',1991)

mercedes.total_cars()


# /----------------- დავალება 17 -----------------