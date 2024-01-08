import unittest
from assignment1 import is_prime, are_relatively_prime, prime_decomposition

class TestAssignment1(unittest.TestCase):
    def test_PrimeDecompositionGivesCorrectAnswerFor1(self):
        self.assertEqual([], prime_decomposition(1))

    def test_PrimeDecompositionGivesCorrectAnswerFor2(self):
        self.assertEqual([2], prime_decomposition(2))

    def test_PrimeDecompositionGivesCorrectAnswerFor23(self):
        self.assertEqual([23], prime_decomposition(23))

    def test_PrimeDecompositionGivesCorrectAnswerFor0(self):
        self.assertEqual([], prime_decomposition(0))

    def test_PrimeDecompositionGivesCorrectAnswerFor14(self):
        self.assertEqual([2,7], prime_decomposition(14))

if __name__=="__main__":
    unittest.main()