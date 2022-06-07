// 4. Which company has the most number of programmers (employees) and how many employees do they have?
MATCH (p:Programmer)-[w:`works for`]->(company:Company)
RETURN company.name as Company, COLLECT(p.firstName) as Programmers, count(p) as NumProgrammers
ORDER BY SIZE(Programmers) DESC LIMIT 10
