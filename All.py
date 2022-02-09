import fastf1
import fastf1 as ff1

year = input("Enter the Year: ")
race = input("Enter Race Name/Number: ")
if type(race) == int:
    raceName = race
    
elif type(race) == float:
    raceName = race

elif type(race) == str:
    raceName = "'" + race + "'"
weekend = ff1.get_session(year, raceName, 'R')
out = fastf1.api.fetch_page(weekend.api_path, 'team_radio')
print(out, indent=4)
