import logging
import unittest
from my_laborotory import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            babulya = Runner("babulya", -3)
            for i in range(10):
                babulya.walk()
            self.assertEqual(babulya.distance,50)
            logging.info("'test_walk' выполнен успешно'")
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            cat = Runner("cat")
            for i in range(10):
                cat.run()
            self.assertEqual(cat.distance, 100)
            logging.info("'test_run' выполнен успешно'")
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        owner = Runner("owner")
        enemy = Runner("enemy")
        for i in range(10):
            owner.walk()
            enemy.run()
        self.assertNotEqual(owner.distance, enemy.distance)

if __name__ == "__main__":
    unittest.main()
    logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w",
                        encoding="UTF-8", format="%(levelname)s | %(message)s")
