import unittest
import sys

from sieve.sieve import sieve_in_interval, calculate_primes_in_interval


class SieveTest(unittest.TestCase):
    def test_valid_values(self):
        res = sieve_in_interval(2, 2)
        self.assertEqual(res, [2])

        res = sieve_in_interval(2, 30)
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

        res = sieve_in_interval(58, 114)
        self.assertEqual(res, ([59, 61, 67, 71, 73, 79, 83,
                                89, 97, 101, 103, 107, 109, 113]))

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            sieve_in_interval(-20, 20)

        with self.assertRaises(ValueError):
            sieve_in_interval(80, 30)


if __name__ == '__main__':
    unittest.main()
