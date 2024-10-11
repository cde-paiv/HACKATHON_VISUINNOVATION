class Route:
	def __init__(self, init_location, mid_location, final_location, emergency_location):
		self.init_location = init_location
		self.mid_location = mid_location
		self.final_location = final_location
		self.emergency_location = emergency_location

	def display_info(self):
		print(f"Route Start: {self.init_location}")
		print(f"Mid Route: {self.mid_location}")
		print(f"Final Destination: {self.final_location}")
		print(f"Emergency Route: {self.emergency_location}")

