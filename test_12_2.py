from my_laborotory import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
    def setUp(self):
        self.run1 = Runner("Усэйн", 10)
        self.run2 = Runner("Андрей", 9)
        self.run3 = Runner("Ник", 3)
    def tests1(self):
        obj1 = Tournament(90, self.run1, self.run3).start()
        self.all_results.append(obj1)
        self.assertEqual(self.all_results[-1][2], "Ник")
    def test2(self):
        obj2 = Tournament(90, self.run2, self.run3).start()
        self.all_results.append(obj2)
        self.assertEqual(self.all_results[-1][2], "Ник")
    def test3(self):
        obj3 = Tournament(90, self.run1, self.run2, self.run3).start()
        self.all_results.append(obj3)
        self.assertEqual(self.all_results[-1][3], "Ник")

    @classmethod
    def tearDownClass(self):
        print(self.all_results[-1])
        print(self.all_results[0])
        print(self.all_results[1])

if __name__ == "__main__":
    unittest.main()
