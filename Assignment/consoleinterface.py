import hotel


class Contoller:
	def __init__(self):
		print ("************ Hotel Applications****************")
	def initalize(self):
		interface = hotel.MasterController()
		user_choice = interface.calloption()



if __name__ == '__main__':
	ctrl = Contoller()

	ctrl.initalize()