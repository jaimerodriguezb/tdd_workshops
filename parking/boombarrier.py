import unittest
from unittest.mock import patch, MagicMock
from drivers import CamDriver, BoomBarrierDriver

class ParkingSystem():
    def __init__(self):
        self.camm_driver = CamDriver()
        self.boombarrier = BoomBarrierDriver()

    def is_plate_paid(self, plate):
        return self.camm_driver.check_car_plate(plate)
    
    def validate_plate(self, plate):
        try:
            payment = self.is_plate_paid(plate)
            if payment == True:
                self.boombarrier.lift()
            elif payment == False:
                self.boombarrier.lower()
        except ValueError:
            print("Please make sure you paid")

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

    @patch.object(CamDriver, "check_car_plate", return_value=True)
    def test_paid(self, mock_check_car_plate):
        plate = 'abc123'
        system = ParkingSystem()
        system.camm_driver.check_car_plate = mock_check_car_plate

        result = system.is_plate_paid(plate)

        self.assertEqual(result, True)

    @patch.object(CamDriver, "check_car_plate", return_value=False)
    def test_unpaid(self, mock_check_car_plate):
        plate = 'abc123'
        system = ParkingSystem()
        system.camm_driver.check_car_plate = mock_check_car_plate

        result = system.is_plate_paid(plate)

        self.assertEqual(result, False)

    @patch.object(CamDriver, "check_car_plate", 
                  side_effect=ValueError("Payment status Undefined"))
    def test_undefined(self, mock_check_car_plate):
        plate = None
        system = ParkingSystem()
        system.camm_driver.check_car_plate = mock_check_car_plate

        with self.assertRaises(ValueError) as error:
            system.is_plate_paid(plate)

        self.assertEqual(error.exception.args[0], "Payment status Undefined")


    @patch("builtins.print")
    @patch.object(CamDriver, "check_car_plate", return_value=True)
    def test_lift(self, mock_check_car_plate, mock_print):
        plate = 'abc123'
        system = ParkingSystem()
        system.camm_driver.check_car_plate = mock_check_car_plate

        system.validate_plate(plate)

        mock_print.assert_called_with("Lifting barrier")

    @patch("builtins.print")
    @patch.object(CamDriver, "check_car_plate", return_value=False)
    def test_lower(self, mock_check_car_plate, mock_print):
        plate = 'abc123'
        system = ParkingSystem()
        system.camm_driver.check_car_plate = mock_check_car_plate

        system.validate_plate(plate)

        mock_print.assert_called_with("Lowering barrier")

    @patch("builtins.print")
    @patch.object(CamDriver, "check_car_plate", 
                  side_effect=ValueError("Payment status Undefined"))
    def test_user_error_message(self, mock_check_car_plate, mock_print):
        plate = None
        system = ParkingSystem()
        system.camm_driver.check_car_plate = mock_check_car_plate

        system.validate_plate(plate)

        mock_print.assert_called_with("Please make sure you paid")

unittest.main(__name__)