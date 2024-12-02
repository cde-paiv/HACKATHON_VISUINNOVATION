from Monitoring import Monitoring
from Waypoint import Waypoint
from Mission import Mission
from mavsdk import System
from pymavlink import mavutil
from Drone import Drone
import asyncio
import csv # testing with a little database
import sys

#	@ print function to test
def			print_values():
	from Weather import Weather
	print(f"drone at {Drone.latitude} {Drone.longitude} {Drone.absolute_altitude}")
	print(f"drone battery: {Drone.battery_level} {Drone.battery_temp}")
	print('Temperature:',Weather.temp,'°C')
	print('Wind:',Weather.wind)
	print('Pressure: ',Weather.pressure)
	print('Humidity: ',Weather.humidity)
	print('Description:',Weather.description)
	print('Visibility:',Weather.visibility)

#	@@ receive the name and the waypoint and search it at the csv
#	@ Temp function that reads the data of the csv and sets the waypoint to fly to
def			finding_points_user(name, waypoint):
	with open('database.csv', 'r') as csvfile:
		csv_reader = csv.reader(csvfile)
		for row in csv_reader:
			if (row[0] == name):
				break
		for row in csv_reader:
			if (row[1] == waypoint):
				Waypoint.latitude = float(row[2])
				Waypoint.longitude = float(row[3])
				Waypoint.altitude = float(row[4])
				print("found == |",row[1], "|")
				return True
	print("Waypoint do not exist, or not in the user")
	return False

#	@@ receive what the program should do and where to go
#	@ test main
async def main():
	print("-- program started --")
	drone = System()

	Drone.drone_id = 14550
	what_to_do = sys.argv[1]
	await drone.connect(system_address="udp://:14550")
	print("-- drone connected")
	if sys.argv[1] == "fly":
		name = sys.argv[2]
		waypoint = sys.argv[3]
		if finding_points_user(name, waypoint) == True:
			await Mission.start_mission(drone)
	if sys.argv[1] == "data":
		await Monitoring.refreshing_values(drone)
		print_values()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
