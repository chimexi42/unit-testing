import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup')
        self.emp_1 = Employee('corey', 'shafer', 5000)
        self.emp_2 = Employee('chima', 'okoro', 6000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')

        self.assertEqual(self.emp_1.email, 'corey.shafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'chima.okoro@gmail.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.shafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.okoro@gmail.com')

    def test_fullname(self):
        print('test_fullname')

        self.assertEqual(self.emp_1.fullname, 'corey shafer')
        self.assertEqual(self.emp_2.fullname, 'chima okoro')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John shafer')
        self.assertEqual(self.emp_2.fullname, 'Jane okoro')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 6300)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/shafer/May')
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()
