// 1. Return what company programmer 'fp210' works for
MATCH (p:Programmer {firstName: 'fp210'})-[w:`works for`]->(c:Company) 
RETURN p.id, c.name