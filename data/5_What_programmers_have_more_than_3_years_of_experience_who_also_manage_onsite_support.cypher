// 5. What programmers have more than 3 years of experience, who also manage onsite support 
// for a python project?
MATCH (oss:Onsitesupport)-[:`provided for`]-(pj:Project{language:'Python'})
MATCH (oss)-[:`managed by`]-(pg:Programmer)
WHERE pg.yearsOfExperience > 3
RETURN oss.id, collect(pg.id) as Programmers, collect(pg.yearsOfExperience) as YearsExperience
