from datetime import datetime
import random
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from shapely.geometry import Point
from objects import *


class Generator():
        def __init__(self, engine: Engine, N_companies: int, N_betatests: int, N_demos: int, N_onsitesupports: int,
         N_clients: int, N_programmers: int, N_salesperson: int, N_users: int, N_projects: int) -> None:
                self.engine = Engine
                self.N_companies = N_companies
                self.N_betatests = N_betatests
                self.N_demos = N_demos
                self.N_onsitesupports = N_onsitesupports
                self.N_clients = N_clients
                self.N_programmers = N_programmers
                self.N_salesperson = N_salesperson
                self.N_users = N_users
                self.N_projects = N_projects
                Session = sessionmaker(engine)  
                self.session = Session()
           
        def genPeople(self):
                for i in range(int(self.N_companies)):
                        p = Person(first_name="fpr"+str(i), last_name="lpr"+str(i))
                        self.session.add(p)
                self.session.commit()

        def genCompanies(self):
                for i in range(int(self.N_companies)):
                        c = Company(name="C"+str(i), ceo=i+1, description="company"+str(i))
                        self.session.add(c)
                self.session.commit()
                #projects, programmers, clients have company id
                #betatests, demos, onsitesupports have company id
     
        def genProgrammers(self):
                for i in range(int(self.N_programmers)):
                        p = Programmer(first_name="fp"+str(i), last_name="lp"+str(i), years_of_experience=i % 7, company_id=random.randint(1, self.N_companies-1))
                        self.session.add(p)
                self.session.commit()
                #projects has programmer list
                #onsitesupports has programmerlist

        def genClients(self):
                companies = self.session.query(Company)
                cs = random.sample(list(companies), random.randint(0, 6))
                for i in range(int(self.N_clients)):
                        c = Client(first_name="fc"+str(i), last_name="lc"+str(i), companies=cs)
                        self.session.add(c)
                self.session.commit()
                #betatests has client list
                #demos has client list

        def genSalespeople(self):
                for i in range(int(self.N_salesperson)):
                        s = Salesperson(first_name="fs"+str(i), last_name="ls"+str(i), trustworthy=bool(random.getrandbits(1)))
                        self.session.add(s)
                self.session.commit()
                #demos has salespeople list

        def genUsers(self):
                for i in range(int(self.N_users)):
                        u = User(first_name="fs"+str(i), last_name="ls"+str(i), age=random.randint(5, 99))
                        self.session.add(u)
                self.session.commit()
                #projects has users list
                #betatests has users list

        def genProjects(self):
                for i in range(int(self.N_programmers)):
                        company=random.randint(1, self.N_companies-1)
                        companies = self.session.query(Company)
                        programmers = companies[company].programmers
                        num_programmers = random.randint(0, len(programmers))
                        ps = random.sample(programmers, num_programmers)

                        us = random.sample(list(self.session.query(User)), random.randint(0, self.N_users/2))

                        languages=["Java", "Python", "Go", "Rust"]
                        lang = languages[random.randint(0, len(languages)-1)]
        
                        p = Project(programmers=ps, users=us, language=lang, in_production=bool(random.getrandbits(1)),
                         description="project"+str(i), company_id=company)
                        self.session.add(p)
                self.session.commit()
                #betatests, demos, onsitesupports have lists


        def genBetaTests(self):
                for i in range(int(self.N_betatests)):
                        project=random.randint(1, self.N_projects)
                        projects = self.session.query(Project)
                        print("\n\n\nproject id is", project)
                        p = projects[project-1]
                        users = list(p.users)
                        num_users = random.randint(0, len(users))
                        us = random.sample(users, num_users)
                        company = projects[project-1].company_id

                        b = BetaTest(location = None,
                        start_time=datetime.fromtimestamp(random.randint(int(datetime.today().timestamp()), int(datetime.today().timestamp()) + 86400)), 
                        end_time=datetime.fromtimestamp(random.randint(int(datetime.today().timestamp()), int(datetime.today().timestamp()) + 86400)),
                        users = us,
                        project_id = project,
                        company_id = company,
                        )
                        self.session.add(b)
                self.session.commit()

        
        def genDemos(self):
                for i in range(int(self.N_demos)):
                        project=random.randint(1, self.N_projects)

                        projects = self.session.query(Project)
                        print("\n\n\nproject id is", project)
                        p = projects[project-1]

                        company = p.company_id

                        companies = self.session.query(Company)
                        cs = random.sample(companies[company-1].clients, random.randint(0, 6))

                        salespeople = self.session.query(Salesperson)
                        sp = random.sample(salespeople, random.randint(0, 4))

                        d = Demo(location=None, 
                        start_time=datetime.fromtimestamp(random.randint(int(datetime.today().timestamp()), int(datetime.today().timestamp()) + 86400)), 
                        end_time=datetime.fromtimestamp(random.randint(int(datetime.today().timestamp()), int(datetime.today().timestamp()) + 86400)),
                        salespeople = sp,
                        project_id = project,
                        company_id = company,
                        clients = cs
                        )
                        self.session.add(d)
                self.session.commit()    

        def genOnSiteSupports(self):
                for i in range(int(self.N_onsitesupports)):
                        project=random.randint(1, self.N_projects)
                        projects = self.session.query(Project)
                        print("\n\n\nproject id is", project)
                        p = projects[project-1]

                        company = p.company_id
                        ps = random.sample(projects[project-1].programmers, random.randint(0, 3))

                        o = OnSiteSupport(location = None,
                        start_time=datetime.fromtimestamp(random.randint(int(datetime.today().timestamp()), int(datetime.today().timestamp()) + 86400)), 
                        end_time=datetime.fromtimestamp(random.randint(int(datetime.today().timestamp()), int(datetime.today().timestamp()) + 86400)),
                        fixed_problem = bool(random.getrandbits(1)),
                        project_id = project,
                        company_id = company,
                        programmers = ps
                        )
                        self.session.add(o)
                self.session.commit()   

        def genAll(self):
                self.genPeople()
                self.genCompanies()
                self.genProgrammers()
                self.genUsers()
                self.genClients()
                self.genSalespeople()
                self.genProjects()
                self.genBetaTests()
                self.genDemos()
                self.genOnSiteSupports()
           