from faker import Faker
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    interior_parts = relationship('InteriorPart', back_populates='car')
    exterior_parts = relationship('ExteriorPart', back_populates='car')

    def __repr__(self):
        return f'Car(id={self.id}, name={self.name})'

class InteriorPart(Base):
    __tablename__ = 'interior_parts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    car_id = Column(Integer, ForeignKey('cars.id'), index=True)
    car = relationship('Car', back_populates='interior_parts')
    

    def __repr__(self):
        return f'interiorPart(id={self.id}'+\
           f'name={self.name}'+\
           f'price ={self.price})'


class ExteriorPart(Base):
    __tablename__ = 'exterior_parts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship('Car', back_populates='exterior_parts')



    def __repr__(self):
        return f'ExteriorPart(id={self.id}'+\
           f'name={self.name}'+\
           f'price ={self.price})'
    


    def __repr__(self):
        return f'Car(id={self.id}'+\
           f'name={self.name})'

if __name__ == '__main__':
    engine = create_engine('sqlite:///parts.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

fake = Faker()
# instances

InteriorPart1= InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart2= InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart3= InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart4= InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart5= InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart6= InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart7 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart8 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart9 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)
InteriorPart10 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart11 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart12 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart13 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart14 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

InteriorPart15 = InteriorPart(
    name=fake.word(),
    price=fake.random_int(min=1000, max=100000)
)

interior_parts = [
        InteriorPart(name=fake.word(), price=fake.random_int(min=1000, max=100000))
        for _ in range(15)
    ]


ExteriorPart1= ExteriorPart(
    name = "Front Bumper",
    price ="35000"
)

ExteriorPart2= ExteriorPart(
    name = "Back bumper",
    price ="21000"
)

ExteriorPart3= ExteriorPart(
    name = "Tail light",
    price ="36100"
)

ExteriorPart4= ExteriorPart(
    name = "Headlight",
    price ="25200"
)

ExteriorPart5= ExteriorPart(
    name = "Roof racks",
    price ="12000"
)

ExteriorPart6= ExteriorPart(
    name = "Side mirrors",
    price ="22000"
)

ExteriorPart7 = ExteriorPart(
    name="Grille",
    price="18000"
)

ExteriorPart8 = ExteriorPart(
    name="Fender",
    price="15000"
)

ExteriorPart9 = ExteriorPart(
    name="Spoiler",
    price="25000"
)

ExteriorPart10 = ExteriorPart(
    name="Hood",
    price="28000"
)

ExteriorPart11 = ExteriorPart(
    name="Wheels",
    price="45000"
)

ExteriorPart12 = ExteriorPart(
    name="Tire covers",
    price="8000"
)

ExteriorPart13 = ExteriorPart(
    name="Window tint",
    price="6000"
)

ExteriorPart14 = ExteriorPart(
    name="Door handles",
    price="7000"
)

ExteriorPart15 = ExteriorPart(
    name="Antenna",
    price="3000"
)

def create_car(name):
    new_car = Car(name=name)
    session.add(new_car)
    session.commit()
    return new_car

def create_interior_part(car_id, name, price):
    car = session.query(Car).get(car_id)
    new_interior_part = InteriorPart(name=name, price=price)
    car.interior_parts.append(new_interior_part)
    session.commit()
    return new_interior_part

def create_exterior_part(car_id, name, price):
    car = session.query(Car).get(car_id)
    new_exterior_part = ExteriorPart(name=name, price=price)
    car.exterior_parts.append(new_exterior_part)
    session.commit()
    return new_exterior_part

def get_car(car_id):
    car = session.query(Car).get(car_id)
    return car

def get_all_cars():
    cars = session.query(Car).all()
    return cars

def get_interior_parts(car_id):
    car = session.query(Car).get(car_id)
    interior_parts = car.interior_parts
    return interior_parts

def get_exterior_parts(car_id):
    car = session.query(Car).get(car_id)
    exterior_parts = car.exterior_parts
    return exterior_parts

def update_car_name(car_id, new_name):
    car = session.query(Car).get(car_id)
    car.name = new_name
    session.commit()
    return car

def update_interior_part_price(interior_part_id, new_price):
    interior_part = session.query(InteriorPart).get(interior_part_id)
    interior_part.price = new_price
    session.commit()
    return interior_part

def update_exterior_part_price(exterior_part_id, new_price):
    exterior_part = session.query(ExteriorPart).get(exterior_part_id)
    exterior_part.price = new_price
    session.commit()
    return exterior_part

def delete_car(car_id):
    car = session.query(Car).get(car_id)
    session.delete(car)
    session.commit()

def delete_interior_part(interior_part_id):
    interior_part = session.query(InteriorPart).get(interior_part_id)
    session.delete(interior_part)

# ...

if __name__ == '__main__':
    engine = create_engine('sqlite:///parts.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    
    new_car = create_car("Subaru")

    
    create_interior_part(new_car.id, "Leather Seats", 2500)
    create_interior_part(new_car.id, "windshield", 3000)

    
    create_exterior_part(new_car.id, "size 15 rims", 4000)
    create_exterior_part(new_car.id, "Sunroof", 2000)

    
    car = get_car(new_car.id)
    print(car)

    
    cars = get_all_cars()
    for car in cars:
        print(car)

    
    interior_parts = get_interior_parts(new_car.id)
    for part in interior_parts:
        print(part)

    
    exterior_parts = get_exterior_parts(new_car.id)
    for part in exterior_parts:
        print(part)

    
    updated_car = update_car_name(new_car.id, "Subaru")
    print(updated_car)

    
    updated_part = update_interior_part_price(interior_parts[0].id, 2800)
    print(updated_part)

    
    updated_part = update_exterior_part_price(exterior_parts[0].id, 4500)
    print(updated_part)

    
    delete_car(new_car.id)

    session.close()


session.add_all([InteriorPart1,InteriorPart2,InteriorPart3,InteriorPart4,InteriorPart5,InteriorPart6,InteriorPart7,InteriorPart8,InteriorPart9,InteriorPart10,InteriorPart11,InteriorPart12,InteriorPart13,InteriorPart14,InteriorPart15])
session.add_all([ExteriorPart1,ExteriorPart2,ExteriorPart3,ExteriorPart4,ExteriorPart5,ExteriorPart6,ExteriorPart7,ExteriorPart8,ExteriorPart9,ExteriorPart10,ExteriorPart11,ExteriorPart12,ExteriorPart13,ExteriorPart14,ExteriorPart15])
session.commit()


