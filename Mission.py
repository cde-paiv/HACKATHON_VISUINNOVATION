from mavsdk.mission import MissionItem, MissionPlan
from Monitoring import Monitoring
from Location import Location
from Waypoint import Waypoint
from mavsdk import System
from Drone import Drone
from Log import log
import asyncio

class Mission:
	STOPPED = 2
	RUNNING = 1
	FINISHED = 0
	ONCE = 1
	UNTIL_END = 0

	def __init__(self, home=None, date=None, waypoints=None, distance=0, id="12345", status=STOPPED, time_start=None, time_end=None):
		self.home = {"latitude": "", "longitude": "", "altitude": ""}
		self.date = None
		self.wapoints = [
							"",
							"",
							"",
							]
		self.distance = 5
		self.id = "a1fgudf456"
		self.distance = 0
		self.status = self.STOPPED
		self.time_start = None
		self.time_end = None

#	@@ Receive the coordinates of the home
#	@ Set drone home position
	def			define_home(self, latitude, longitude, altitude):
		self.home["latitude"] = latitude
		self.home["longitude"] = longitude
		self.home["altitude"] = altitude

#	@@ Receive the drone entity
#	@ Fuction set the log and the monitoring to run and start the mission
	async def	start_mission(drone):
			print("-- Starting_Mision")
			if await Mission.mission_manage(drone) == True:
				monitoring = asyncio.create_task(Monitoring.monitoring_misson_n_drone(drone))
				log_file = asyncio.create_task(log())
				await Mission.drone_fly(drone)
				monitoring.cancel()
				await asyncio.sleep(10)
				log_file.cancel()
				return True
			else:
				#write message(cant start the flight now, try again later)
				return False


#	@@ Receive the drone entity
#	@ Check the conditions to see if the drone can fly
	async def	mission_manage(drone):
			if await Monitoring.first_comparation(drone) == True:
				return True
			print("===========One or more parameters are not great to fly===========")
			return False


#	@@ Receive the drone, the position which it is going to and the tolarance
#	@ Countinously compare the drone position to the target one, until it reaches the tolerance
	async def wait_until_position_reached(drone, target_lat, target_lon, target_alt, tolerance):
		Location.latitude = target_lat
		Location.longitude = target_lon
		Location.altitude = target_alt
		while True:
			print(Location.calc_distance(Drone, Location))
			if (Location.calc_distance(Drone, Location) <= tolerance):
				break
			await asyncio.sleep(0.5)


#	@@ Receive the drone entity
#	@ Do the hole flight from home to the Waypoint desired and return to home
	async def drone_fly(drone):
		mission = Mission()
		Mission.status = Mission.RUNNING
		mission.define_home(Drone.latitude, Drone.longitude, Drone.absolute_altitude)

		print("Arming...")
		await drone.action.arm()

		print("Taking off...")
		await drone.action.set_takeoff_altitude(Waypoint.altitude)
		await drone.action.takeoff()
		await Mission.wait_until_position_reached(Drone, Drone.latitude, Drone.longitude, Waypoint.altitude, 3.00)

		print("Going to location...")
		await drone.action.goto_location(Waypoint.latitude, Waypoint.longitude, Waypoint.altitude, 0)
		await Mission.wait_until_position_reached(Drone, Waypoint.latitude, Waypoint.longitude, Waypoint.altitude, 0.5)

		print("Return to launch...")
		await drone.action.return_to_launch()
		await Mission.wait_until_position_reached(Drone, mission.home['latitude'], mission.home['longitude'], Drone.absolute_altitude, 0.5)

		print("Landing...")
		await drone.action.land()
		await Mission.wait_until_position_reached(Drone, mission.home['latitude'], mission.home['longitude'], mission.home['altitude'], 0.5)

		Mission.status = Mission.FINISHED
		print("Program ending.")

