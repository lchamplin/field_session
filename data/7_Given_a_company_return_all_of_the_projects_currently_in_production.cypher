// 7. Given a company, return all of the projects currently in production
// Degree 1, high number of specific properties to search through
MATCH (company:Company{id:11})-[r:`belongs to`] -(pj:Project{inProduction:'true'})
RETURN pj.id as projectsNotInProduction,company.name as Company
