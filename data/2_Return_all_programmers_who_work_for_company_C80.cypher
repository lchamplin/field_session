// 2. Return all programmers who work for company 'C80'
MATCH (p:Programmer)-[w:`works for`]->(c:Company{name: 'C80'}) 
RETURN p.id as ProgrammerID, c.name as CompanyName