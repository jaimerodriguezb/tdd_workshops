import unittest
from drivers import CamDriver, BoomBarrierDriver

class ParkingSystem():
    def __init__(self):
        self.camm = CamDriver()

    def is_plate_paid(self, plate):
        return self.camm.check_car_plate(plate)


def validate_payment(plate, payment):
    if plate and payment:
        return 'LIFT'
    elif plate and (not payment or 
                    type(payment) is not int or 
                    (type(payment) is int and payment <=0)):
        return 'NO PAYMENT'
    elif not plate:
        raise (ValueError('UNDEFINED PLATE'))

# Design using plain functional description

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
        
# Design using the drivers
class BoomBarrierUsingDriverTest(unittest.TestCase):

    def test_paid(self):
        plate = 'abc123'
        system = ParkingSystem()

        result = system.is_plate_paid(plate)

        self.assertEqual(result, 'OK')

unittest.main(__name__)