from Location import Location

class Package:
	def __init__(self, location: Location, destination: Location, status, package_load):
		self.location = location
		self.destination = destination
		self.status = status
		self.package_load = package_load

	def update_status(self, new_status):
		self.status = new_status
		print(f"Package status updated to: {self.status}")

	def display_info(self):
		print(f"Package Current Location: {self.location.latitude}, {self.location.longitude}, Altitude: {self.location.altitude}")
		print(f"Package Destination: {self.destination.latitude}, {self.destination.longitude}, Altitude: {self.destination.altitude}")
		print(f"Package Status: {self.status}")
		print(f"Package Load: {self.package_load}kg")

