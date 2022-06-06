import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('corey', 'shafer', 5000)
        emp_2 = Employee('chima', 'okoro', 6000)

        self.assertEqual(emp_1.email, 'corey.shafer@gmail.com')
        self.assertEqual(emp_2.email, 'chima.okoro@gmail.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.shafer@gmail.com')
        self.assertEqual(emp_2.email, 'Jane.okoro@gmail.com')

    def test_fullname(self):
        emp_1 = Employee('corey', 'shafer', 5000)
        emp_2 = Employee('chima', 'okoro', 6000)

        self.assertEqual(emp_1.fullname, 'corey shafer')
        self.assertEqual(emp_2.fullname, 'chima okoro')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John shafer')
        self.assertEqual(emp_2.fullname, 'Jane okoro')

    def test_apply_raise(self):
        emp_1 = Employee('corey', 'shafer', 5000)
        emp_2 = Employee('chima', 'okoro', 6000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 5250)
        self.assertEqual(emp_2.pay, 6300)


if __name__ == '__main__':
    unittest.main()
