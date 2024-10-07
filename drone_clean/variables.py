from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan
import requests
import asyncio
import sys

ONCE = 1
FINISHED = 0
UNTIL_END = 0

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
		print(f"Current Location: {self.location.latitude}, {self.location.longitude}, Altitude: {self.location.altitude}")
		print(f"Max Load Capacity: {self.max_load}kg")
		print(f"Current Load: {self.current_load}kg")
		print(f"Battery Level: {self.battery_level}%")
		print(f"Status: {self.status}")

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

class Mission:
	def __init__(self):
		Mission.wapoints = [
							"",
							"",
							"",
							]
		Mission.distance = 5
		Mission.id = "a1fgudf456"
		Mission.distance = 0
		Mission.status = "FINISHED"

class Ideal_params:
	#====weather====#
	VISIBILITY = 100
	# PRESSURE = 120000 #se necessario?
	HUMIDITY = 80 # 80%
	WIND = 10 # m/s
	DESCRIPTION = [
					"Clear",
					"Cloudy",
					"",
					"",
					"",
					"",
					"",]
	MIN_TEMP = 278
	MAX_TEMP = 318
	#=====battery=====#
	MIN_BATTERY_TAKEOFF = 80 # minimo para comecar o voo e ainda fazer o checker se eh possivel voar com isso
	MIN_BATTERY_IN_FLIGHT = 30
	BATTERY_TEMP_MIN = 283
	BATTERY_TEMP_MAX = 333
	#======drone======#
	MAX_BASE_DISTANCE = 8000 # 8km
	MAX_ABSOLUTE_ALTITUDE = 4500
	MIN_REALTIVE_ALTITUDE = 10
	MAX_REALTIVE_ALTITUDE = 120
	MAXIMUM_TAKEOFF_MASS = 29.0 # drone + gadgets + shipment
	MAXIMUM_TAKEOFF_OPEN_MASS = 24.9 # drone + gadgets + shipment

class Weather:
	def __init__(self, pressure, humidity, wind, description, temp, visibility):
		Weather.humidity = humidity
		Weather.pressure = pressure
		Weather.wind = wind
		Weather.description = description
		Weather.temp = temp
		Weather.visibility = visibility

	def	get_weather(latitude_deg, longitude_deg):
		company_key = "039abd108da2d28ed7c29abf82966f2f"
		src = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude_deg}&lon={longitude_deg}&appid={company_key}"

		return_req = requests.get(src)
		data = return_req.json()
		Weather.humidity = data['main']['humidity']
		Weather.pressure = data['main']['pressure']
		Weather.wind = data['wind']['speed']
		Weather.description = data['weather'][0]['description']
		Weather.temp = data['main']['temp']
		Weather.visibility  = data['visibility']

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

def		print_values():
		print(f"drone at {Drone.latitude} {Drone.longitude}")
		print(f"drone battery: {Drone.battery_level}")
		print('Temperature:',Weather.temp,'°C')
		print('Wind:',Weather.wind)
		print('Pressure: ',Weather.pressure)
		print('Humidity: ',Weather.humidity)
		print('Description:',Weather.description)
		print('Visibility:',Weather.visibility)


