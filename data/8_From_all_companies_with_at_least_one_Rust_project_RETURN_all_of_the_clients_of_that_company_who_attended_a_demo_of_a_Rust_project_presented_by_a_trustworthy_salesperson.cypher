// 8. From all companies with at least one Rust project,
// RETURN all of the clients of that company who attended a demo of a
// Rust project presented by a trustworthy salesperson
MATCH (d:Demo)-[r:demoing]->(p:Project{language:'Rust'})
MATCH (d)-[:`presented by`]->(tw:Salesperson{trustworthy:'true'})
MATCH (c:Client)-[:attends]->(d)
RETURN DISTINCT c