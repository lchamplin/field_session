// 11. Returning all projects which user 1 uses
MATCH (u:User_P {id: 1})-[r:`designed for`]-(p:Project)
RETURN u,p
