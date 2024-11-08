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

	def calc_distance(location, other_location):
		import math

		lat1_rad = math.radians(location.latitude)
		long1_rad = math.radians(location.longitude)
		lat2_rad = math.radians(other_location.latitude)
		long2_rad = math.radians(other_location.longitude)

		a = (
			math.sin((lat2_rad - lat1_rad) / 2) ** 2
			+ math.cos(lat1_rad) * math.cos(lat2_rad)
			* math.sin((long2_rad - long1_rad) / 2) ** 2
		)

		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

		horizontal_distance = 6371000 * c

		altitude_difference = (other_location.altitude - location.absolute_altitude)

		total_distance = math.sqrt(horizontal_distance**2 + altitude_difference**2)

		return total_distance
