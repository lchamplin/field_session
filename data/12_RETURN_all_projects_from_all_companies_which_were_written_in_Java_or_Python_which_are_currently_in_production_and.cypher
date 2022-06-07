// 12. RETURN all projects from all companies which were written in Java or Python which are currently in production and 
// for which there are more than 2 programmers managing onsite support
MATCH (J_OSS)-[m1:`managed by`]->(jp:Programmer)
WITH J_OSS,count(jp) as jpCount
WHERE jpCount > 2

MATCH (J_OSS:Onsitesupport)-[:`provided for`]->(J_proj:Project{inProduction:'true',language:'Java'})

RETURN J_proj.id as ProjID

UNION ALL

MATCH (P_OSS)-[m2:`managed by`]->(pp:Programmer)
WITH P_OSS,count(pp) as ppCount
WHERE ppCount > 2

MATCH (P_OSS:Onsitesupport)-[:`provided for`]->(P_proj:Project{inProduction:'true',language:'Python'})

RETURN P_proj.id as ProjID