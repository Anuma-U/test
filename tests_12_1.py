import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        babulya = Runner("babulya")
        for i in range(10):
            babulya.walk()
        self.assertEqual(babulya.distance,50)

    def test_run(self):
        cat = Runner("cat")
        for i in range(10):
            cat.run()
        self.assertEqual(cat.distance, 100)

    def test_challenge(self):
        owner = Runner("owner")
        enemy = Runner("enemy")
        for i in range(10):
            owner.walk()
            enemy.run()
        self.assertNotEqual(owner.distance, enemy.distance)

if __name__ == "__main__":
    unittest.main()
