// 8-2. Different approach
MATCH (d:Demo)-[r:demoing]->(p:Project{language:'Rust'})
MATCH (d)-[:`presented by`]->(tw:Salesperson{trustworthy:'true'})
MATCH (c:Client)-[:attends]->(d)
RETURN SIZE(collect(DISTINCT c))