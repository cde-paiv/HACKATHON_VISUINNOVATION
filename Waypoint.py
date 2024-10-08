from User import User

class Waypoint:
	def __int__(self, latitude: float, longitude: float, altitude: float, wayPoint_name):
		self.latitude = latitude
		self.longitude = longitude
		self.altitude = altitude
		self.wayPoint_name = wayPoint_name

	def add_waypoint(self, wayPoint_name: str, latitude: float, longitude: float, altitude: float):
		user = User()
		user.waypoint = Waypoint(wayPoint_name, latitude, longitude, altitude)
		self.waypoints.append(waypoint)

	def remove_waypoint(self, wayPoint_name: str):
		self.waypoints = [wp for wp in self.waypoints if wp.wayPoint_name != wayPoint_name]
