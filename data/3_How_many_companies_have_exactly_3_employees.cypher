// 3. How many companies have exactly 3 employees
MATCH (p:Programmer)-[w:`works for`]->(c:Company) 
WITH c, count(p) as employees
WHERE employees = 3
RETURN count(employees) as NumCompaniesWith3Employees
