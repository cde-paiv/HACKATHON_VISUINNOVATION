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
