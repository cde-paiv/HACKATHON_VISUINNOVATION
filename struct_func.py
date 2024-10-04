from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan
import datetime #logfile
import requests
import asyncio
import sys

# to monitor, we will nede one function that will refresh the values of the variables and one to check them
ONCE = 1
UNTIL_END = 0
FINISHED = 0
RUNNING = 1
STOPPED = 2

class Drone:
	def __init__(self, drone, drone_id, latitude, longitude, max_load, status, relative_altitude, absolute_altitude, flight_mode, battery_level = 100, current_load = 0):
		self.drone = drone
		self.drone_id = drone_id
		self.max_load = max_load
		self.status = status
		self.battery_level = battery_level
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

"""
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
		self.way_points = way_points

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

 """
#============================================================================================#
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
		Mission.status = STOPPED


#============================================================================================#
class Ideal_params:
	PRESSURE = 120000
	HUMIDITY = 120000
	WIND = 120000
	DESCRIPTION = [
					"Clear",
					"Cloudy",
					"",
					"",
					"",
					"",
					"",]
	TEMP = 120000
	BATTERY = 10
	VISIBILITY = 100


#============================================================================================#
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


#============================================================================================#
def		print_values():
		print(f"drone at {Drone.latitude} {Drone.longitude}")
		print(f"drone battery: {Drone.battery_level}")
		print('Temperature:',Weather.temp,'°C')
		print('Wind:',Weather.wind)
		print('Pressure: ',Weather.pressure)
		print('Humidity: ',Weather.humidity)
		print('Description:',Weather.description)
		print('Visibility:',Weather.visibility)

async def	creating_detailed_log():
	time_beg = datetime.datetime.now()
	with open("flight_log.txt", "a") as log_file:
		log_header = f"\n"
		log_file.write(log_header)
		while 1:
			log_entry = f"{Drone.latitude}, {Drone.longitude}, {Drone.relative_altitude}\n"
			log_file.write(log_entry)
			if Mission.status == FINISHED:
				break
			await asyncio.sleep(1)
		time_end = datetime.datetime.now()
		log_footer = f"=====> Drone flight ended, started at {time_beg} ended at {time_end}, so it took {time_end - time_beg}\n"
		log_file.write(log_footer)


#============================================================================================#
# after add the mission values here, so can be checked as well

async def	monitoring_misson_n_drone(drone, flag):
	while 1:
		await refreshing_values(drone)
		if await comparing_values() == False:
			print("One or more parameters are not great to")
			break
		print_values()
		# Here is going to be the actions that depending on the the return of the comparing_values
		# will happen. -----(if the params are not good, flyback)------(if they are terrible, land_Now)------
		if flag == ONCE:
			return (True)
		if Mission.status == FINISHED:
			return (True)

async def	comparing_values():
	if Weather.humidity > Ideal_params.HUMIDITY:
		return False
	if Weather.wind > Ideal_params.WIND:
		return False
	if Weather.pressure > Ideal_params.PRESSURE:
		return False
	if Weather.visibility < Ideal_params.VISIBILITY:
		return False
	if Drone.battery_level < Ideal_params.BATTERY:
		return False
	#for param in Ideal_params.DESCRIPTION:
	#	if param == Weather.description:
	#		return True
	return True

async def	refreshing_values(drone):
	async for battery in drone.telemetry.battery():
		break
	async for position in drone.telemetry.position():
		break
	Drone.latitude = position.latitude_deg
	Drone.longitude = position.longitude_deg
	Drone.absolute_altitude = position.absolute_altitude_m
	Drone.relative_altitude = position.relative_altitude_m
	Drone.battery_level = battery.remaining_percent
	Weather.get_weather(position.latitude_deg, position.longitude_deg)


#============================================================================================#
async def	mission_manage(drone):
		if await monitoring_misson_n_drone(drone, ONCE) == True:
			return True
		print("-------------falso-----------")
		return False


async def	drone_fly(mission, drone):
		mission_plan = MissionPlan(mission.mission_itens)
		await drone.mission.set_return_to_launch_after_mission(True)
		await drone.mission.upload_mission(mission_plan)
		await drone.action.arm()
		await drone.action.takeoff(drone.altitute_to_fly)
		await drone.mission.start_mission()


async def	start_mission(drone):
		print("-- Starting_Mision")
		if await mission_manage(drone) == True:
			#mission_plan = MissionbPlan(mission.mission_itens)
			monitoring = asyncio.create_task(monitoring_misson_n_drone(drone, UNTIL_END))
			log_file = asyncio.create_task(creating_detailed_log())
			#await drone_fly(drone, mission)
			await drone_fly_test(drone)
			monitoring.cancel()
			log_file.cancel()
			return True
		else:
			#write message(cant start the flight now, try again later)
			return False


def			cancel_mission(drone):
		drone.FlightMode.RETURN_TO_LAUNCH() # never used this one, need to be tested
		# await drone.action.return_to_launch()


async def	drone_fly_test(drone):
	print("Arming...")
	Mission.status = RUNNING
	await drone.action.arm()
	await drone.action.set_takeoff_altitude(590.0)
	print("taking off...")
	await drone.action.takeoff()
	await asyncio.sleep(10)
	print("going to location...")
	await drone.action.goto_location(-35.362633, 149.163448, 590.0, 0.0)
	await asyncio.sleep(30)
	print("return to launch...")
	await drone.action.return_to_launch()
	await asyncio.sleep(30)
	print("landing...")
	await drone.action.land()
	print("program ending")
	await asyncio.sleep(10)
	Mission.status = FINISHED


#============================================================================================#
async def main():
	print("-- program started --")
	drone = System()

	await drone.connect(system_address="udp://:14550")
	print("-- drone connected")
	if sys.argv[1] == '1':
		await start_mission(drone)
	if sys.argv[1] == '2': # test the updating of the values and compare them with the ideal ones
		await monitoring_misson_n_drone(drone, ONCE)
		#print_values()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
