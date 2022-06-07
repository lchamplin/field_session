// 9. Given a company, RETURN all of the programmers who 
// manage onsite support for all projects written in RUST at that company 
MATCH (C492:Company{name:'C492'})<-[r:`belongs to`]-(rp:Project{language:'Rust'})
MATCH (rp)<-[:`provided for`]-(oss:Onsitesupport)
MATCH (pg:Programmer)-[:`managed by`]-(oss)
RETURN pg.id as programmer, C492.id as company, rp.id as RustProject, oss.id as onSiteSupportID