// 10. How many users use project 623? ANS: 36
MATCH (u:User_P)-[r:`designed for`]-(p:Project {id:623})
WITH count(u) as Num_Users_of_Proj_623
RETURN Num_Users_of_Proj_623
