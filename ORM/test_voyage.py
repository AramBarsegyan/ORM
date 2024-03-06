import unittest
from sqlalchemy.inspection import inspect
from comp.voyage import Voyage
from comp.ship import Ship
from database import SessionLocal, init_db
from methods import BaseMethod

class TestVoyageMethods(unittest.TestCase):
    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.voyage_method = BaseMethod(self.session, Voyage)
        self.test_ship = Ship(ship_name="Test Ship")
        self.session.add(self.test_ship)
        self.session.commit()

    def test_get(self):
        voyage = Voyage(voyage_number="VY100", destination="Hawaii", ship_id=self.test_ship.id)
        self.session.add(voyage)
        self.session.commit()

        retrieved = self.voyage_method.get(voyage.id)
        self.assertEqual(voyage, retrieved)

    def test_find(self):
        voyage1 = Voyage(voyage_number="VM101", destination="Alaska", ship_id=self.test_ship.id)
        voyage2 = Voyage(voyage_number="VS202", destination="Bahamas", ship_id=self.test_ship.id)
        self.session.add(voyage1)
        self.session.add(voyage2)
        self.session.commit()

        results = self.voyage_method.find(destination="Alaska")
        self.assertIn(voyage1, results)
        self.assertNotIn(voyage2, results)

    def test_get_all(self):
        voyage1 = Voyage(voyage_number="VC303", destination="Caribbean", ship_id=self.test_ship.id)
        voyage2 = Voyage(voyage_number="VE404", destination="Mediterranean", ship_id=self.test_ship.id)
        self.session.add(voyage1)
        self.session.add(voyage2)
        self.session.commit()

        all_records = self.voyage_method.get_all()
        self.assertIn(voyage1, all_records)
        self.assertIn(voyage2, all_records)

    def test_save(self):
        voyage = Voyage(voyage_number="VN505", destination="Norwegian Fjords", ship_id=self.test_ship.id)
        self.voyage_method.save(voyage)

        saved_record = self.voyage_method.get(voyage.id)
        self.assertEqual(saved_record, voyage)

    def test_delete(self):
        voyage = Voyage(voyage_number="VB606", destination="Baltic Sea", ship_id=self.test_ship.id)
        self.session.add(voyage)
        self.session.commit()

        self.voyage_method.delete(voyage)
        self.assertIsNone(self.voyage_method.get(voyage.id))

    def tearDown(self):
        self.session.query(Voyage).delete()  # Удаляем все записи из таблицы voyage
        self.session.query(Ship).delete()  # Удаляем все записи из таблицы ship для соблюдения целостности
        self.session.commit()
        self.session.close()

    def test_voyage_table_mapping(self):
        voyage_mapper = inspect(Voyage)
        self.assertEqual(voyage_mapper.local_table.name, "voyage")

if __name__ == '__main__':
    unittest.main()
