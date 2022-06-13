#!/usr/bin/env python

import time
from sqlalchemy.orm import sessionmaker
from objects import *
from sqlalchemy import select
from sqlalchemy import text

import psycopg2


def main():
        engine = create_engine('postgresql://postgres:mypassword@fsdatabase.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)
        # engine = create_engine('postgresql://postgres:mypassword@fsdatabase1.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)
        # engine = create_engine('postgresql://postgres:mypassword@fsdatabase2.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)

        Session = sessionmaker(engine)  
        session = Session()

       
        # # 1 Return what company programmer 'fp210' works for
        # textual_sql = text("SELECT * from company WHERE id=(SELECT company_id FROM programmer WHERE first_name='fp210')")
        # for i in session.execute(textual_sql):
        #         print(i)

#         # 2 Return all programmers who work for company 'C80'
        # textual_sql = text("SELECT * from programmer WHERE company_id = (SELECT id from company WHERE name='C80')")
        # for i in session.execute(textual_sql):
        #         print(i)

#         # 3 How many companies have exactly 3 employees
        # textual_sql = text("SELECT COUNT(*) from company WHERE 3=(SELECT COUNT(*) FROM programmer WHERE programmer.company_id = company.id)")
        # for i in session.execute(textual_sql):
        #         print(i)

#         # 4 Which company has the most number of programmers (employees) and how many employees do they have?
        # textual_sql = text("SELECT COUNT(*), company_id FROM programmer GROUP BY company_id ORDER BY COUNT(*) DESC LIMIT 10")
        # for i in session.execute(textual_sql):
        #         print(i)

        
#          # 5 What programmers have more than 3 years of experience, who also manage onsite support for a python project?
        # textual_sql = text("SELECT DISTINCT programmer.first_name, programmer.last_name, onsitesupport.project_id FROM programmer, onsitesupport, project, onsitesupport_programmer_association"
        # +" WHERE programmer.years_of_experience > 3 AND programmer.id=onsitesupport_programmer_association.programmer_id AND onsitesupport.id = onsitesupport_programmer_association.onsitesupport_id"
        # +" AND onsitesupport.project_id IN (SELECT id FROM project WHERE language='Python')")
        # for i in session.execute(textual_sql):
        #         print(i)

#         # 6 Given a client, return all the projects written in Rust for which the client attended a demo of the project
#         client_id = 1001
#         textual_sql = text("SELECT project.id FROM project, demo, demo_client_association"
#        +" WHERE "+str(client_id)+" =demo_client_association.client_id AND demo.id=demo_client_association.demo_id"
#        +" AND demo.project_id = project.id AND project.language='Rust'")
#         for i in session.execute(textual_sql):
#                 print(i)

#         # 7. Given a company, return all of the projects currently in production
        # company_id = 11
        # textual_sql = text("SELECT DISTINCT project.id FROM company, project WHERE project.company_id = "+str(company_id)+" AND project.in_production='1'")
        # for i in session.execute(textual_sql):
        #         print(i)

#         # 8 From all companies with at least one Rust project, RETURN all of the clients of that company who attended a demo of a Rust project presented by a trustworthy salesperson
        # textual_sql = text("SELECT COUNT(DISTINCT client.id) FROM client, client_company_association as cca, demo_client_association as dca WHERE client.id=cca.client_id AND cca.company_id IN (SELECT id FROM company WHERE ( (SELECT COUNT(*) FROM project WHERE company_id=company.id AND language='Rust') > 0)) AND client.id = dca.client_id"
        # + " AND dca.demo_id IN (SELECT DISTINCT demo.id FROM demo, salesperson, demo_salesperson_association AS dsa WHERE demo.project_id IN (SELECT id FROM project WHERE language='Rust') AND demo.id = dsa.demo_id AND salesperson.id = dsa.salesperson_id AND salesperson.trustworthy = '1')")
        # for i in session.execute(textual_sql):
        #         print(i)




#         # 9. Given a company, RETURN all of the programmers who manage onsite support for all projects written in RUST at that company 
        # company_name = 'C492'
        # textual_sql = text("SELECT DISTINCT programmer.first_name FROM programmer, onsitesupport, onsitesupport_programmer_association AS opa, project_programmer_association AS ppa, project, company"
        # +" WHERE onsitesupport.id = opa.onsitesupport_id AND programmer.id = opa.programmer_id AND onsitesupport.project_id = ppa.project_id AND ppa.programmer_id = programmer.id"
        # + " AND project.language = 'Rust' AND project.company_id IN (SELECT id FROM company WHERE name='"+company_name+"')")
        # for i in session.execute(textual_sql):
        #         print(i)


# #         # 10. How many user_ps use project 623?
#         textual_sql = text("SELECT COUNT(DISTINCT user_p.id) FROM user_p, project, project_user_association AS pua WHERE pua.project_id=623 AND pua.user_id = user_p.id" )
#         for i in session.execute(textual_sql):
#                 print(i)


        # 11. Returning all projects which user_p 1 uses
        # textual_sql = text("SELECT DISTINCT(project.id) FROM user_p, project, project_user_association AS pua WHERE pua.user_id=1 AND pua.project_id = project.id")
        # for i in session.execute(textual_sql):
        #         print(i)


#         # 12 RETURN all projects from all companies which were written in Java or Python 
#         # which are currently in production and for which there are more than 2 programmers managing onsite support
        textual_sql = text("SELECT project.id FROM project WHERE project.in_production='1' AND (language='Java' OR language='Python')"
        +" AND (SELECT COUNT(DISTINCT programmer.id) FROM programmer, onsitesupport, onsitesupport_programmer_association AS opa WHERE opa.programmer_id = programmer.id"
        +" AND onsitesupport.project_id = project.id) > 1")
        for i in session.execute(textual_sql):
                print(i)


main()