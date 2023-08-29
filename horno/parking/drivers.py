class CamDriver():
	def __init__(self):
		self.cammera_connection = None

	def check_car_plate(self, plate):
		payment_status = self.cammera_connection.read_payment_status()
		if payment_status == 'OK':
			return True
		elif payment_status == 'PENDING':
			return False
		else:
			raise ValueError("Payment status Undefined")


class BoomBarrierDriver():
	def __init__(self):
		self.barries_connection = None

	def lift(self):
		print('Lifting barrier')

	def lower(self):
		print('Lowering barrier')