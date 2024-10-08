class User:
	def __init__(self, user_id, status, drone_id, way_points):
		self.user_id = user_id
		self.status = status
		self.drone_id = drone_id
		self.waypoints = []

	def update_status(self, new_status):
		self.status = new_status
		print(f"User status updated to: {self.status}")

	def display_info(self):
		print(f"User ID: {self.user_id}")
		print(f"User Status: {self.status}")
		print(f"User Drone ID: {self.drone_id}")
		print(f"User Way Points:")

		for index, waypoint in enumerate(self.way_points, start=1):
			print(f"Waypoint {index}: {waypoint[0]}, {waypoint[1]}, {waypoint[2]}")

