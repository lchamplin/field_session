// 6. Given a client, return all the projects written in Rust for which the client attended a demo of the project
// Degree 2 query, with specific properties of objects
MATCH (client:Client{id:1001})-[r:attends]-(demos:Demo)-[r2:demoing]-(rustProjects:Project{language:'Rust'})
RETURN rustProjects.id as RustProject, client.id as Client, demos.id as Demo