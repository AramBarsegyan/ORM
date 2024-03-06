from database import SessionLocal, init_db
from methods import BaseMethod
from comp.ship import Ship
from comp.voyage import Voyage

# Создание таблиц
init_db()

# Создание сессии
session = SessionLocal()

ship_repository = BaseMethod(session, Ship)
voyage_repository = BaseMethod(session, Voyage)

# Добавление данных о судах
titanic = Ship(ship_name="Titanic")
queen_mary = Ship(ship_name="Queen Mary")
symphony_of_the_seas = Ship(ship_name="Symphony of the Seas")
viking_sky = Ship(ship_name="Viking Sky")
ship_repository.save(titanic)
ship_repository.save(queen_mary)
ship_repository.save(symphony_of_the_seas)
ship_repository.save(viking_sky)

# Добавление данных о маршрутах
voyage1 = Voyage(voyage_number="VY101", destination="Barcelona", ship_id=1)
voyage2 = Voyage(voyage_number="QM256", destination="New York", ship_id=2)
voyage3 = Voyage(voyage_number="SO345", destination="Miami", ship_id=3)
voyage4 = Voyage(voyage_number="VK464", destination="Oslo", ship_id=4)
voyage_repository.save(voyage1)
voyage_repository.save(voyage2)
voyage_repository.save(voyage3)
voyage_repository.save(voyage4)

# Вывод информации о маршрутах и судах
all_voyages = voyage_repository.get_all()
for voyage in all_voyages:
    ship = ship_repository.get(voyage.ship_id)
    print(f"Номер маршрута: {voyage.voyage_number}")
    print(f"Место назначения: {voyage.destination}")
    print(f"Имя судна: {ship.ship_name}")
    print("-" * 50)

session.close()
