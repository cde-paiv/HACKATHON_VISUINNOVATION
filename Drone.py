class Drone:
	def __init__(self, drone, drone_id, latitude, longitude, max_load, status, relative_altitude, absolute_altitude, flight_mode, battery_temp, battery_level, current_load = 0):
		self.drone = drone
		self.drone_id = drone_id
		self.max_load = max_load
		self.status = status
		self.battery_level = battery_level
		self.battery_temp = battery_temp
		self.current_load = current_load
		self.latitude = latitude
		self.longitude = longitude
		self.absolute_altitude = absolute_altitude
		self.relative_altitude = relative_altitude
		self.fligh_mode = flight_mode

	def max_distance_possible(self):
		from Ideal_Params import Ideal_params
		max_distance = Ideal_params.FULL_LOADED_BATTERY * (self.battery_level / 100) * Ideal_params.DIST_PER_W
		return max_distance

	def update_battery_level(self, new_battery_level):
		self.battery_level = new_battery_level
		print(f"Drone battery updated to:{self.battery_level}")

	def update_status(self, new_status):
		self.status = new_status
		print(f"Drone status updated to: {self.status}")

	def update_location(self, location):
		self.location = location
		print(f"Drone {self.drone_id} location updated to {self.location}")

	def display_info(self):
		print(f"Drone ID: {self.drone_id}")
		print(f"Current Location: {self.latitude}, {self.longitude}, Altitude: {self.location.altitude}")
		print(f"Max Load Capacity: {self.max_load}kg")
		print(f"Current Load: {self.current_load}kg")
		print(f"Battery Level: {self.battery_level}%")
		print(f"Status: {self.status}")

