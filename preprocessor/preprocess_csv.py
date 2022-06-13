import pandas
uid_offset = 0

#PERSON
df = pandas.read_csv('csv/person.csv')
df = df.rename(columns={"id": "uid"})
df["dgraph.type"] = "Person"

uid_offset += df.shape[0]
df.to_csv('person.csv', index=False)  

#COMPANY
df = pandas.read_csv('csv/company.csv')
df = df.rename(columns={"id": "uid"})
df["dgraph.type"] = "Company"
df["uid"] = df["uid"] + uid_offset
uid_offset_company = uid_offset
#ceo id stays same because person uid
uid_offset += df.shape[0]
df.to_csv('company.csv', index=False)  

#PROGRAMMER
df = pandas.read_csv('csv/programmer.csv')
df = df.rename(columns={"id": "uid"})
df["dgraph.type"] = "Programmer"
df["uid"] = df["uid"] + uid_offset
uid_offset_programmer = uid_offset
df["company_id"] = df["company_id"] + uid_offset_company
df = df.rename(columns={"company_id": "uid"})

uid_offset += df.shape[0]
df.to_csv('programmer.csv', index=False)  

#USER
df = pandas.read_csv('csv/user_p.csv')
df["dgraph.type"] = "User"
df = df.rename(columns={"id": "uid"})
df["uid"] = df["uid"] + uid_offset
uid_offset_user = uid_offset

uid_offset += df.shape[0]
df.to_csv('user_p.csv', index=False)  

#CLIENT
df = pandas.read_csv('csv/clients.csv')
df["dgraph.type"] = "Client"
df = df.rename(columns={"id": "uid"})
df["uid"] = df["uid"] + uid_offset
uid_offset_client = uid_offset

uid_offset += df.shape[0]
df.to_csv('client.csv', index=False)  

#SALESPERSON
df = pandas.read_csv('csv/salesperson.csv')
df["dgraph.type"] = "Salesperson"
df = df.rename(columns={"id": "uid"})
df["uid"] = df["uid"] + uid_offset
uid_offset_salesperson = uid_offset

uid_offset += df.shape[0]
df.to_csv('salesperson.csv', index=False)  

#PROJECT
df = pandas.read_csv('csv/project.csv')
df["dgraph.type"] = "Project"
df = df.rename(columns={"id": "uid"})
df["uid"] = df["uid"] + uid_offset
uid_offset_project = uid_offset
df["company_id"] = df["company_id"] + uid_offset_company
df = df.rename(columns={"company_id": "uid"})

uid_offset += df.shape[0]
df.to_csv('project.csv', index=False)  


#BETATEST
df = pandas.read_csv('csv/betatest.csv')
df["dgraph.type"] = "Betatest"
df = df.rename(columns={"id": "uid"})
df["uid"] = df["uid"] + uid_offset
uid_offset_betatest = uid_offset
df["company_id"] = df["company_id"] + uid_offset_company
df = df.rename(columns={"company_id": "uid"})
df["project_id"] = df["project_id"] + uid_offset_project
df = df.rename(columns={"project_id": "uid"})

uid_offset += df.shape[0]
df.to_csv('betatest.csv', index=False)  


#DEMO
df = pandas.read_csv('csv/demo.csv')
df["dgraph.type"] = "Demo"
df = df.rename(columns={"id": "uid"})
df["uid"] = df["uid"] + uid_offset
uid_offset_demo = uid_offset
df["company_id"] = df["company_id"] + uid_offset_company
df = df.rename(columns={"company_id": "uid"})
df["project_id"] = df["project_id"] + uid_offset_project
df = df.rename(columns={"project_id": "uid"})

uid_offset += df.shape[0]
df.to_csv('demo.csv', index=False)  


#ONSITESUPPORT
df = pandas.read_csv('csv/onsitesupport.csv')
df["dgraph.type"] = "Onsitesupport"
df = df.rename(columns={"id": "uid"})
df["uid"] = df["uid"] + uid_offset
uid_offset_onsitesupport = uid_offset
df["company_id"] = df["company_id"] + uid_offset_company
df = df.rename(columns={"company_id": "uid"})
df["project_id"] = df["project_id"] + uid_offset_project
df = df.rename(columns={"project_id": "uid"})

uid_offset += df.shape[0]
df.to_csv('onsitesupport.csv', index=False) 


#BETATEST-USER
df = pandas.read_csv('csv/betatest_user_association.csv')
df["betatest_id"] = df["betatest_id"] + uid_offset_betatest
df["user_id"] = df["user_id"] + uid_offset_user
df = df.rename(columns={"betatest_id": "uid"})
df = df.rename(columns={"user_id": "uid"})
df.to_csv('betatest_user_association.csv', index=False) 

#CLIENT-COMPANY
df = pandas.read_csv('csv/client_company_association.csv')
df["client_id"] = df["client_id"] + uid_offset_client
df["company_id"] = df["company_id"] + uid_offset_company
df = df.rename(columns={"client_id": "uid"})
df = df.rename(columns={"company_id": "uid"})
df.to_csv('client_company_association.csv', index=False) 

#DEMO-CLIENT
df = pandas.read_csv('csv/demo_client_association.csv')
df["demo_id"] = df["demo_id"] + uid_offset_demo
df["client_id"] = df["client_id"] + uid_offset_client
df = df.rename(columns={"demo_id": "uid"})
df = df.rename(columns={"client_id": "uid"})
df.to_csv('demo_client_association.csv', index=False) 

#DEMO-SALESPERSON
df = pandas.read_csv('csv/demo_salesperson_association.csv')
df["demo_id"] = df["demo_id"] + uid_offset_demo
df["salesperson_id"] = df["salesperson_id"] + uid_offset_salesperson
df = df.rename(columns={"demo_id": "uid"})
df = df.rename(columns={"salesperson_id": "uid"})
df.to_csv('demo_salesperson_association.csv', index=False) 

#ONSITESUPPORT-PROGRAMMER
df = pandas.read_csv('csv/onsitesupport_programmer_association.csv')
df["onsitesupport_id"] = df["onsitesupport_id"] + uid_offset_onsitesupport
df["programmer_id"] = df["programmer_id"] + uid_offset_programmer
df = df.rename(columns={"onsitesupport_id": "uid"})
df = df.rename(columns={"programmer_id": "uid"})
df.to_csv('onsitesupport_programmer_association.csv', index=False) 

#PROJECT-PROGRAMMER
df = pandas.read_csv('csv/project_programmer_association.csv')
df["project_id"] = df["project_id"] + uid_offset_project
df["programmer_id"] = df["programmer_id"] + uid_offset_programmer
df = df.rename(columns={"project_id": "uid"})
df = df.rename(columns={"programmer_id": "uid"})
df.to_csv('project_programmer_association.csv', index=False) 

#PROJECT-USER
df = pandas.read_csv('csv/project_user_association.csv')
df["project_id"] = df["project_id"] + uid_offset_project
df["user_id"] = df["user_id"] + uid_offset_programmer
df = df.rename(columns={"project_id": "uid"})
df = df.rename(columns={"user_id": "uid"})
df.to_csv('project_user_association.csv', index=False) 