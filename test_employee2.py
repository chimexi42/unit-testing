import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('corey', 'shafer', 5000)
        self.emp_2 = Employee('chima', 'okoro', 6000)

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'corey.shafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'chima.okoro@gmail.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.shafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.okoro@gmail.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'corey shafer')
        self.assertEqual(self.emp_2.fullname, 'chima okoro')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John shafer')
        self.assertEqual(self.emp_2.fullname, 'Jane okoro')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 6300)


if __name__ == '__main__':
    unittest.main()
