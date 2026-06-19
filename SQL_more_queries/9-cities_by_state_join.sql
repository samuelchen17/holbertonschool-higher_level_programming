-- list all cities in DB
SELECT cities.id, cities.name, state.name 
FROM cities JOIN state
ON cities.state_id = state.id
SORT BY cities.id ASC;