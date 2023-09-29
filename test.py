import requests
instance_prompt = """
Here is a database schema:
department :
Department_ID [ INT ] primary_key
Name [ TEXT ]
Creation [ TEXT ]
Ranking [ INT ]
Budget_in_Billions [ REAL ]
Num_Employees [ REAL ]

head :
head_ID [ INT ] primary_key
name [ TEXT ]
born_state [ TEXT ]
age [ REAL ]

management :
department_ID [ INT ] primary_key management.department_ID=department.Department_ID
head_ID [ INT ] management.head_ID=head.head_ID
temporary_acting [ TEXT ]

Please write me a SQL statement that answers the following question: How many heads of the departments are older than 56 ? [/INST] select count ( * ) from head where age > 56; [INST] Here is a database schema:
book_club :
book_club_id [ INT ] primary_key
Year [ INT ]
Author_or_Editor [ TEXT ]
Book_Title [ TEXT ]
Publisher [ TEXT ]
Category [ TEXT ]
Result [ TEXT ]

culture_company :
Company_name [ TEXT ] primary_key
Type [ TEXT ]
Incorporated_in [ TEXT ]
Group_Equity_Shareholding [ REAL ]
book_club_id [ TEXT ] culture_company.book_club_id=book_club.book_club_id
movie_id [ TEXT ] culture_company.movie_id=movie.movie_id

movie :
movie_id [ INT ] primary_key
Title [ TEXT ]
Year [ INT ]
Director [ TEXT ]
Budget_million [ REAL ]
Gross_worldwide [ INT ]

Please write me a SQL statement that answers the following question: What are all company names that have a corresponding movie directed in the year 1999? [/INST] select culture_company.company_name from movie inner join culture_company on movie.movie_id = culture_company.movie_id where movie.year = 1999; [INST] Here is a database schema:
station :
id [ INTEGER ] primary_key
name [ TEXT ]
lat [ NUMERIC ]
long [ NUMERIC ]
dock_count [ INTEGER ]
city [ TEXT ]
installation_date [ TEXT ]

status :
station_id [ INTEGER ] status.station_id=station.id
bikes_available [ INTEGER ]
docks_available [ INTEGER ]
time [ TEXT ]

trip :
id [ INTEGER ] primary_key
duration [ INTEGER ]
start_date [ TEXT ]
start_station_name [ TEXT ]
start_station_id [ INTEGER ]
end_date [ TEXT ]
end_station_name [ TEXT ]
end_station_id [ INTEGER ]
bike_id [ INTEGER ]
subscription_type [ TEXT ]
zip_code [ INTEGER ]

weather :
date [ TEXT ]
max_temperature_f [ INTEGER ]
mean_temperature_f [ INTEGER ]
min_temperature_f [ INTEGER ]
max_dew_point_f [ INTEGER ]
mean_dew_point_f [ INTEGER ]
min_dew_point_f [ INTEGER ]
max_humidity [ INTEGER ]
mean_humidity [ INTEGER ]
min_humidity [ INTEGER ]
max_sea_level_pressure_inches [ NUMERIC ]
mean_sea_level_pressure_inches [ NUMERIC ]
min_sea_level_pressure_inches [ NUMERIC ]
max_visibility_miles [ INTEGER ]
mean_visibility_miles [ INTEGER ]
min_visibility_miles [ INTEGER ]
max_wind_Speed_mph [ INTEGER ]
mean_wind_speed_mph [ INTEGER ]
max_gust_speed_mph [ INTEGER ]
precipitation_inches [ INTEGER ]
cloud_cover [ INTEGER ]
events [ TEXT ]
wind_dir_degrees [ INTEGER ]
zip_code [ INTEGER ]

Please write me a SQL statement that answers the following question: What are the ids of stations that have latitude above 37.4 and never had bike availability below 7? [/INST] select id from station where lat > 37.4 except select station_id from status group by station_id having min ( bikes_available ) < 7; [INST] Here is a database schema:
concert :
concert_ID [ INT ] primary_key
concert_Name [ TEXT ]
Theme [ TEXT ]
Stadium_ID [ TEXT ] concert.Stadium_ID=stadium.Stadium_ID
Year [ TEXT ]

singer :
Singer_ID [ INT ] primary_key
Name [ TEXT ]
Country [ TEXT ]
Song_Name [ TEXT ]
Song_release_year [ TEXT ]
Age [ INT ]
Is_male [ bool ]

singer_in_concert :
concert_ID [ INT ] primary_key singer_in_concert.concert_ID=concert.concert_ID
Singer_ID [ TEXT ] singer_in_concert.Singer_ID=singer.Singer_ID

stadium :
Stadium_ID [ INT ] primary_key
Location [ TEXT ]
Name [ TEXT ]
Capacity [ INT ]
Highest [ INT ]
Lowest [ INT ]
Average [ INT ]

Please write me a SQL statement that answers the following question: {question}
Do not provide any commentary or explanation of what the code does, just the SQL statement ending in a semicolon.
"""
question = """What are the names, themes, and number of singers for every concert?"""
prompt_codellama2 = instance_prompt.format(question=question) + "\nAnswer: "


import time
b = time.time()
a = requests.post("http://0.0.0.0:8080/process_message", json={"message": prompt_codellama2})   

print(f"time: {time.time() -b}s")