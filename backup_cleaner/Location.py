class Location:
	def __init__(self, latitude, longitude, altitude=0):
		self.latitude = latitude
		self.longitude = longitude
		self.altitude = altitude

	def update_location(self, new_latitude, new_longitude, new_altitude):
		self.latitude = new_latitude
		self.longitude = new_longitude
		if new_altitude is not None:
			self.altitude = new_altitude
		print(f"Location updated to: ({self.latitude}, {self.longitude}, {self.altitude}m)")

	def calc_distance(self, other_location):
		from math import sqrt

		distance = sqrt(
			(self.latitude - other_location.latitude) ** 2 +
			(self.longitude - other_location.longitude) ** 2 +
			(self.altitude - other_location.altitude) ** 2
		)
		return distance
