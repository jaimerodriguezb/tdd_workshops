import unittest

def validate_payment(plate, payment):
    return 'LIFT'

class BoomBarrierTest(unittest.TestCase):

    def test_carplate_payment_ok(self):
        plate = 'abc123'
        payment = 5000

        result = validate_payment(plate, payment)

        self.assertEqual(result, 'LIFT')

    def test_carplate_ok_payment_fail(self):
        plate = 'abc123'
        payment = None

        result = validate_payment(plate, payment)

        self.assertEqual(result, 'NO PAYMENT')

unittest.main(__name__)