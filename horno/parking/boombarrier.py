import unittest

def validate_payment(plate, payment):
    if plate and payment:
        return 'LIFT'
    elif plate and (not payment or 
                    type(payment) is not int or 
                    (type(payment) is int and payment <=0)):
        return 'NO PAYMENT'

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

    def test_carplate_undefined(self):
        plate = None
        payment = None

        with self.assertRaises(ValueError):
            validate_payment(plate, payment)
        

unittest.main(__name__)