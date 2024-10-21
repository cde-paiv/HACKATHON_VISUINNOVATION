from mavsdk.mission import MissionItem, MissionPlan
from Monitoring import Monitoring
from Waypoint import Waypoint
from mavsdk import System
from Log import log
import asyncio
from Drone import Drone

class Mission:
	STOPPED = 2
	RUNNING = 1
	FINISHED = 0
	ONCE = 1
	UNTIL_END = 0

	def __init__(self):
		Mission.date = None
		Mission.wapoints = [
							"",
							"",
							"",
							]
		Mission.distance = 5
		Mission.id = "a1fgudf456"
		Mission.distance = 0
		Mission.status = Mission.STOPPED
		Mission.time_start = None
		Mission.time_end = None


#	@ Ativa o modo rtl instantaneamente, cancelando a missao
	async def		cancel_mission(drone):
		await drone.action.returnto_launch()


#	@ checa os parametros para ver se pode voar
	async def	mission_manage(drone):
			if await Monitoring.first_comparation(drone) == True:
				return True
			print("===========One or more parameters are not great to fly===========")
			return True


#	@@ tem que criar ela completa, funcionando para varios ponto e nao dependente de sleep
#	@ missao final de voo
	async def	drone_fly(mission, drone):
			mission_plan = MissionPlan(mission.mission_itens)
			await drone.mission.set_return_to_launch_after_mission(True)
			await drone.mission.upload_mission(mission_plan)
			await drone.action.arm()
			await drone.action.takeoff(drone.altitute_to_fly)
			await drone.mission.start_mission()


#	@ função que começa e missao e ativa o monitoramento asincrono
	async def	start_mission(drone):
			print("-- Starting_Mision")
			if await Mission.mission_manage(drone) == True:
				monitoring = asyncio.create_task(Monitoring.monitoring_misson_n_drone(drone))
				log_file = asyncio.create_task(log())
				#await drone_fly(drone, mission)
				await Mission.drone_fly_test(drone)
				monitoring.cancel()
				await asyncio.sleep(10)
				log_file.cancel()
				return True
			else:
				#write message(cant start the flight now, try again later)
				return False

# verifica continuamente a posição atual do drone até que ele atinja a posição desejada 
	async def wait_until_position_reached(drone, target_lat, target_lon, target_alt, tolerance=0.5):
		while True:
			if (abs(Drone.latitude - target_lat) < tolerance and
          				abs(Drone.longitude - target_lon) < tolerance and
            			abs(Drone.relative_altitude - target_alt) < tolerance):
					print("Posição alcançada.")
					break
			await asyncio.sleep(1)


#	função de voo implementada sem o sleep so falta implemnetar a função de distancia
#	@ função de teste de voô
	async def drone_fly_test(drone):
		print("Arming...")
		Mission.status = Mission.RUNNING
		await drone.action.arm()
		await drone.action.set_takeoff_altitude(Waypoint.altitude)
		print("Taking off...")
		await drone.action.takeoff()
		await Mission.wait_until_position_reached(drone, Waypoint.latitude, Waypoint.longitude, Waypoint.altitude)
		print("Going to location...")
		await drone.action.goto_location(Waypoint.latitude, Waypoint.longitude, Waypoint.altitude, 0)
		await Mission.wait_until_position_reached(drone, Waypoint.latitude, Waypoint.longitude, Waypoint.altitude)
		print("Return to launch...")
		await drone.action.return_to_launch()
		home_position = await anext(drone.telemetry.home())
		await Mission.wait_until_position_reached(drone, home_position.latitude_deg, home_position.longitude_deg, 0)
		print("Landing...")
		await drone.action.land()
		Mission.status = Mission.FINISHED
		print("Program ending.")