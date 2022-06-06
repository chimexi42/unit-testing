import unittest
import main2


class TestMain(unittest.TestCase):

    def test_add(self):
        # result = main2.add(10, 5)
        self.assertEqual(main2.add(10, 5), 15)
        self.assertEqual(main2.add(-1, 1), 0)
        self.assertEqual(main2.add(-1, -1), -2)

    def test_subtract(self):
        # result = main2.add(10, 5)
        self.assertEqual(main2.subtract(10, 5), 5)
        self.assertEqual(main2.subtract(-1, 1), -2)
        self.assertEqual(main2.subtract(-1, -1), 0)

    def test_multiply(self):
        # result = main2.add(10, 5)
        self.assertEqual(main2.multiply(10, 5), 50)
        self.assertEqual(main2.multiply(-1, 1), -1)
        self.assertEqual(main2.multiply(-1, -1), 1)

    def test_divide(self):
        # result = main2.add(10, 5)
        self.assertEqual(main2.divide(10, 5), 2)
        self.assertEqual(main2.divide(-1, 1), -1)
        self.assertEqual(main2.divide(-1, -1), 1)
        self.assertEqual(main2.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            main2.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
