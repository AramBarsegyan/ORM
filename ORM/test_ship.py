import unittest
from sqlalchemy.inspection import inspect
from sqlalchemy.exc import IntegrityError
from comp.ship import Ship
from comp.voyage import Voyage
from database import SessionLocal, init_db
from methods import BaseMethod

class TestShipMethods(unittest.TestCase):
    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.ship_method = BaseMethod(self.session, Ship)

    def test_get(self):
        ship = Ship(ship_name="Titanic")
        self.session.add(ship)
        self.session.commit()

        retrieved = self.ship_method.get(ship.id)
        self.assertEqual(ship, retrieved)

    def test_find(self):
        ship1 = Ship(ship_name="Queen Mary")
        ship2 = Ship(ship_name="Symphony of the Seas")
        self.session.add(ship1)
        self.session.add(ship2)
        self.session.commit()

        results = self.ship_method.find(ship_name="Queen Mary")
        self.assertIn(ship1, results)
        self.assertNotIn(ship2, results)

    def test_get_all(self):
        ship1 = Ship(ship_name="Viking Sky")
        ship2 = Ship(ship_name="Carnival Sunshine")
        self.session.add(ship1)
        self.session.add(ship2)
        self.session.commit()

        all_records = self.ship_method.get_all()
        self.assertIn(ship1, all_records)
        self.assertIn(ship2, all_records)

    def test_save(self):
        ship = Ship(ship_name="Norwegian Bliss")
        self.ship_method.save(ship)

        saved_record = self.ship_method.get(ship.id)
        self.assertEqual(saved_record, ship)

    def test_delete(self):
        ship = Ship(ship_name="Harmony of the Seas")
        self.session.add(ship)
        self.session.commit()

        self.ship_method.delete(ship)
        self.assertIsNone(self.ship_method.get(ship.id))

    def tearDown(self):
        self.session.query(Voyage).delete()  # Удаляем все записи из таблицы voyage для соблюдения целостности
        self.session.query(Ship).delete()  # Удаляем все записи из таблицы ship
        self.session.commit()
        self.session.close()

    def test_ship_table_mapping(self):
        ship_mapper = inspect(Ship)
        self.assertEqual(ship_mapper.local_table.name, "ship")

if __name__ == '__main__':
    unittest.main()
