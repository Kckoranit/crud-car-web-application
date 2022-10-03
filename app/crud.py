from .database import database, countries
from .schema import Car

class CRUD:
    
    def create(self, car: Car):
        n = len(database)
        database.update({n+1: car.dict()})
    
    def read_all_cars(self):
        cars = []
        for id, car in list(database.items()):
            cars.append((id, car))
        return cars 
    
    def read_all_countries(self):
        ct = []
        for i,j in list(countries.items()):
            ct.append((i, j))
        return ct
    
    def read_car_by_id(self, id: int):
        return database.get(id)
    
    def update(self, id: int, car: Car):
        stored_car_data = database[id]
        stored_car_model = Car(**stored_car_data)
        update_car_data = car.dict(exclude_unset=True)
        update_car = stored_car_model.copy(update=update_car_data)
        database[id] = update_car.dict()
    
    def delete(self, id: int):
        del database[id]
        
        
crud = CRUD()