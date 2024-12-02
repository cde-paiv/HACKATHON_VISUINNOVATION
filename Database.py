from supabase import create_client, Client
from dotenv import load_dotenv
import os

class Supabase:
	def	__init__(self, link=None, key=None):
		self.link = "https://vxmmktelugsjuwarwdcv.supabase.co"
		self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ4bW1rdGVsdWdzanV3YXJ3ZGN2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjk1MzU1ODUsImV4cCI6MjA0NTExMTU4NX0.E0BZD7uOhEZoP0CIWEzrruNy1gucC2uEOBqjj7sZhP8"

	#	@@ Receive what is going to be updated in the table and where it should be updated
	#	@ Update the value in the table
	def	Update_table_info(self, table, id, column, new_info):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table(table)
				.update({column: new_info})
				.eq("id", id)
				.execute()
				)

	#	@@ Receive the parameters in order to create and attribute values to a new Waypoint row and the row number
	#	@ Create the new Row with the params passed to it
	def	Create_Waypoint_row(self, id, type, name, lat, long, alt):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
			supabase.table("Waypoint")
			.insert({"id": id, "Type": type, "Name": name, "Latitude":lat, "Longitude":long, "Altitude":alt})
			.execute()
			)

	#	@@ Receive the parameters in order to create and attribute values to a new User row and the row number
	#	@ Create the new User with the params passed to it
	def	Create_User_row(self, id, username, e_mail, password, first_name, last_name, drone_id, waypoint_id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
			supabase.table("User")
			.insert({"id": id, "Username": username, "e-mail": e_mail, "Password":password, "First_name":first_name, "Last_name":last_name, "Drone_ID":drone_id, "Waypoint":waypoint_id})
			.execute()
			)

	#	@@ Receive the table and the id
	#	@ Create an empty row in the assigned table
	def	Create_row(self, table, id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table("table")
				.insert({"id", id})
				.execute()
				)

	#	@@ Receive the table and the row id
	#	@ Delete the received row at a table
	def	Delete_row(self, table, id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response =	(
				supabase.table(table).
				delete()
				.eq('id', id)
				.execute()
				)

	#	@@ Receive the id and the table
	#	@ Access and row info and put it to a variable
	def	Read_row(self, table, row_id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table(table)
				.select("*")
				.eq("id", row_id)
				.execute()
				)

		return response

	#	@@ Receive the table name
	#	@ Take the table info and return it
	def	Read_table(self, table):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table(table)
				.select("*")
				.execute()
				)
		return response

	#	@@ Receive mission_id which the drone is supposed to do
	#	@ The function searches for the mission_id in the mission table and attribute the coordinates to the waypoints
	def	Def_params_mission(self, mission_id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)
		response = supabase.table("Mission").select("*").eq("id", mission_id).execute()

		print(response)
		if response.data:
			record = response.data[0]
			# Drone.drone_id = record.get('Drone_id')
			drone_id = record.get('Drone_id')
			Type_of_delivery = record.get('Type_of_delivery')
			Waypoint = record.get('Waypoint')
			Home = record.get('Home')

			print(drone_id)
			print(Type_of_delivery)
			print(Waypoint)
			print(Home)

		response1 = supabase.table("Waypoint").select("*").eq("id", Waypoint).execute()
		response2 = supabase.table("Waypoint").select("*").eq("id", Home).execute()

		if response1.data:
			record = response1.data[0]
			latitude_w = record.get('Latitude')
			longitude_w = record.get('Longitude')
			altitude_w = record.get('Altitude')
		if response2.data:
			record = response1.data[0]
			latitude_h = record.get('Latitude')
			longitude_h = record.get('Longitude')
			altitude_h = record.get('Altitude')


def	main():
	sup = Supabase()
	print(sup.Read_row("Waypoint", "2"))


main()
