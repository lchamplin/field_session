// 8. From all companies with at least one Rust project, RETURN all of the clients of that company who attended a demo of a // Rust project presented by a trustworthy salesperson
MATCH (companies)<-[r:`belongs to`]-(rustProjects:Project{language:'Rust'})
MATCH (clients)-[h:hires]->(companies)
MATCH (rustDemos:Demo)-[d:demoing]->(rustProjects)
MATCH (twSalesPeople:Salesperson{trustworthy:'true'})
MATCH ((rustDemos)-[:`presented by`]-(twSalesPeople))
MATCH (clients)-[:attends]->(rustDemos)
RETURN SIZE(collect(DISTINCT clients))
