import unittest
from my_laborotory import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        babulya = Runner("babulya")
        for i in range(10):
            babulya.walk()
        self.assertEqual(babulya.distance,50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        cat = Runner("cat")
        for i in range(10):
            cat.run()
        self.assertEqual(cat.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        owner = Runner("owner")
        enemy = Runner("enemy")
        for i in range(10):
            owner.walk()
            enemy.run()
        self.assertNotEqual(owner.distance, enemy.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
    def setUp(self):
        self.run1 = Runner("Усэйн", 10)
        self.run2 = Runner("Андрей", 9)
        self.run3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def tests1(self):
        obj1 = Tournament(90, self.run1, self.run3).start()
        self.all_results.append(obj1)
        self.assertEqual(self.all_results[-1][2], "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        obj2 = Tournament(90, self.run2, self.run3).start()
        self.all_results.append(obj2)
        self.assertEqual(self.all_results[-1][2], "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        obj3 = Tournament(90, self.run1, self.run2, self.run3).start()
        self.all_results.append(obj3)
        self.assertEqual(self.all_results[-1][3], "Ник")



if __name__ == "__main__":
    unittest.main()
