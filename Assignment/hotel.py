class Hotel:
	def __init__(self):
		self.name  = None
		self.rooms = []
	def add_room(self):
		room_name = input("Enter room name ")
		tv =   input("Enter tv y and n ")
		couch = input("Enter couch y and n ")
		table = input("Enter table y and n ")
		air_cond = input("Enter air cond. y and n ")
		budget  = int(input("budget"))
		

		self.rooms.append({"name": room_name, 
						   "budget": budget,
						   "air_cond": air_cond,
						   "table": table,
						   "tv":tv,
						   "couch":couch})
	# def __str__(self):
	# 	return ("%s --- %s ---- %s --- %s --- %s --- %s " % (self.name, self.budget, self.air_cond, self.table, self.tv, self.couch))


class MasterController:
	def __init__(self):
		self.hotel_li = []
		self.hotel_names = []
	
	def addHotel(self):
		hotel = Hotel()
		proceed = True
		while proceed: 
			name_hotel  = input("Enter Hotel name ")
			if name_hotel in self.hotel_names:
				print("name is already exists")
			else:
				self.hotel_names.append(name_hotel)
				proceed = False

		hotel.name = name_hotel

		print ("Want to enter rooms details  Press Y or N ")
		choice  = input("enter your choice")
		if choice.upper() == 'Y':
			cont = 'Y'
			while cont == 'Y':
				self.addrooms(hotel)
				cont = input("Y/N for add another room")
		# else:
		# 	self.calloption()

		self.calloption()

	def addrooms(self, hotel_obj):
		hotel_obj.add_room()
		self.hotel_li.append(hotel_obj)
		

	def calloption(self):
		
		op = int(input("Enter option to continue : \
					\n 1: Feed hotel details  \
					\n 2: print List of hotel  \
					\n 3: print count of hotel \
					\n 4: Details of hotel room  \
					\n 5: Enter customer budget  \
					\n 6: to Exit \
					\n : __________________________\n"))
		if op  == 1:
			self.addHotel()

		elif op == 2:
			if self.hotel_names:
				print ("\n".join(self.hotel_names))
			else:
				print ("Currently we donot have any hotel present")
			self.calloption()

		elif op == 3:
			print ("no of available hotels  ::%d " %  len(self.hotel_names))
			self.calloption()
		
		elif op == 4:
			name = input("hotel name")
			exist  = False
			for details in self.hotel_li:
				if details.name  == name:
					for each in details.rooms:
						for k in each.keys():
							print (k +" ::: "+ str(each[k]))
						print ("----------------------------------")
					self.calloption()
					exist = True
			if not exist:
				print ("hotet not avail. with the name ")

			self.calloption()
		
		elif op == 5:
			budget = input("Enter room budget")
			for each in self.hotel_li:
				for rm in each.rooms:
					print (" ".join([each + str(rm[each]) for each in rm.keys ]))


		elif op == 6:
			print ("Bye bye ...........")
			return

		else:
			print ("Invalid Enteries ....")
			self.calloption()