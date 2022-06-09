#!/usr/bin/env python

import time
from sqlalchemy.orm import sessionmaker
from objects import *
from sqlalchemy import select
from sqlalchemy import text

import psycopg2


def main():
        # engine = create_engine('postgresql://postgres:mypassword@fsdatabase.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)
        engine = create_engine('postgresql://postgres:mypassword@fsdatabase1.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)

        Session = sessionmaker(engine)  
        session = Session()


        queries = [
                "SELECT * from company WHERE id=(SELECT company_id FROM programmer WHERE first_name='fp210')",
                "SELECT * from programmer WHERE company_id = (SELECT id from company WHERE name='C80')",
                "SELECT COUNT(*) from company WHERE 3=(SELECT COUNT(*) FROM programmer WHERE programmer.company_id = company.id)",
                "SELECT COUNT(*), company_id FROM programmer GROUP BY company_id ORDER BY COUNT(*) DESC LIMIT 10",
                "SELECT DISTINCT programmer.first_name, programmer.last_name, onsitesupport.project_id FROM programmer, onsitesupport, project, onsitesupport_programmer_association WHERE programmer.years_of_experience > 3 AND programmer.id=onsitesupport_programmer_association.programmer_id AND onsitesupport.id = onsitesupport_programmer_association.onsitesupport_id AND onsitesupport.project_id IN (SELECT id FROM project WHERE language='Python')",
                "SELECT project.id FROM project, demo, demo_client_association WHERE 1001 =demo_client_association.client_id AND demo.id=demo_client_association.demo_id AND demo.project_id = project.id AND project.language='Rust'",
                "SELECT DISTINCT project.id FROM company, project WHERE project.company_id = 11 AND project.in_production='1'",
                "SELECT COUNT(DISTINCT client.id) FROM client, client_company_association as cca, demo_client_association as dca WHERE client.id=cca.client_id AND cca.company_id IN (SELECT id FROM company WHERE ( (SELECT COUNT(*) FROM project WHERE company_id=company.id AND language='Rust') > 0)) AND client.id = dca.client_id AND dca.demo_id IN (SELECT DISTINCT demo.id FROM demo, salesperson, demo_salesperson_association AS dsa WHERE demo.project_id IN (SELECT id FROM project WHERE language='Rust') AND demo.id = dsa.demo_id AND salesperson.id = dsa.salesperson_id AND salesperson.trustworthy = '1')",
                "SELECT DISTINCT programmer.first_name FROM programmer, onsitesupport, onsitesupport_programmer_association AS opa, project_programmer_association AS ppa, project, company WHERE onsitesupport.id = opa.onsitesupport_id AND programmer.id = opa.programmer_id AND onsitesupport.project_id = ppa.project_id AND ppa.programmer_id = programmer.id AND project.language = 'Rust' AND project.company_id IN (SELECT id FROM company WHERE name='C492')",
                "SELECT COUNT(DISTINCT user_p.id) FROM user_p, project, project_user_association AS pua WHERE pua.project_id=623 AND pua.user_id = user_p.id",
                "SELECT project.id FROM user_p, project, project_user_association AS pua WHERE pua.user_id=1 AND pua.project_id = project.id",
                "SELECT project.id FROM project WHERE project.in_production='1' AND (language='Java' OR language='Python') AND (SELECT COUNT(DISTINCT programmer.id) FROM programmer, onsitesupport, onsitesupport_programmer_association AS opa WHERE opa.programmer_id = programmer.id AND onsitesupport.project_id = project.id) > 1",
        ]

        times = []
        n_repeats = 100
        for query in queries:
                print(query)
                total = 0
                for _ in range(n_repeats):
                        textual_sql = text(query)
                        start = time.time()
                        session.execute(textual_sql)
                        end = time.time()
                        total+=(end - start)
                times.append(total*1000/n_repeats)
        i = 1
        for t in times:
                print("query", i, t)
                i+=1



main()



#  10k database results, 6/7
# query 1 57.539870738983154
# query 2 50.044236183166504
# query 3 213.95848512649536
# query 4 51.65649890899658
# query 5 70.52381992340088
# query 6 58.43841314315796
# query 7 53.07670831680298
# query 8 154.30482864379883
# query 9 167.08465576171875
# query 10 68.11129331588745
# query 11 449.52423572540283
# query 12 83.14294338226318



#  100k database results
# query 1 67.45977640151978
# query 2 54.423439502716064
# query 3 9614.941718578339
# query 4 55.69192886352539
# query 5 735.3175497055054
# query 6 51.61729574203491
# query 7 53.112971782684326
# query 8 52.757487297058105
# query 9 791.3985705375671
# query 10 252.70577907562256
# query 11 4150.944991111755
# query 12 2303.4826970100403