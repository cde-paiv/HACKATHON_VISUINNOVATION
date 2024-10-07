from variables import Mission
from variables import Drone
from variables import FINISHED
import datetime
import asyncio

def creating_log_file(name):
		open(name, "x")

async def writting_simple_log(file):
		with open(file, "a") as simple_log:
			log_header = f"Drone {Drone.drone_id}\nTime of flight {Mission.time_end - Mission.time_start}\nStatus: {Mission.status}\n"
			simple_log.write(log_header)

async def	writting_detailed_log(file):
	with open(file, "a") as det_log:
		log_header = f"Drone {Drone.drone_id} starting flight {Mission.time_start}\n"
		det_log.write(log_header)
		while 1:
			log_entry = f"{Drone.latitude}, {Drone.longitude}, {Drone.relative_altitude}\n"
			det_log.write(log_entry)
			if Mission.status == FINISHED:
				break
			await asyncio.sleep(1)
		Mission.time_end = datetime.datetime.now()
		log_footer = f"=====> Drone flight ended, started at {Mission.time_start} ended at {Mission.time_end}, so it took {Mission.time_end - Mission.time_start}\n"
		det_log.write(log_footer)

async def log():
	Mission.time_start = datetime.datetime.now()
	Mission.date = datetime.date.today()
	simple_log = f"simple_log{Mission.date}{Mission.time_start}.txt"
	detailed_log = f"det_log{Mission.date}{Mission.time_start}.txt"
	creating_log_file(simple_log)
	creating_log_file(detailed_log)
	await writting_detailed_log(detailed_log)
	await writting_simple_log(simple_log)

