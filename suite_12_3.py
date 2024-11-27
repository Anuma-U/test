import unittest
from unittest import TestLoader

import test_12_2
import tests_12_1
import tests_12_3

#part 1

suitTST = unittest.TestSuite()
suitTST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
suitTST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suitTST)

#part 2

froze_tests = unittest.TestSuite()
froze_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
froze_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(froze_tests)