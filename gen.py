from datetime import datetime
import random
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from shapely.geometry import Point
import geoalchemy2
from objects import *


class Generator():
        def __init__(self, engine: Engine, N_companies: int, N_betatests: int, N_demos: int, N_onsitesupports: int,
         N_clients: int, N_programmers: int, N_salesperson: int, N_users: int, N_projects: int, iteration: int) -> None:
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
                self.iteration = iteration
           
        def genPeople(self):
                for i in range(self.iteration*self.N_companies, (self.iteration+1)*self.N_companies):
                        p = Person(first_name="fpr"+str(i), last_name="lpr"+str(i))
                        self.session.add(p)
                self.session.commit()

        def genCompanies(self):
                for i in range(self.iteration*self.N_companies, (self.iteration+1)*self.N_companies):
                        c = Company(name="C"+str(i), ceo=i+1, description="company"+str(i))
                        self.session.add(c)
                self.session.commit()
                #projects, programmers, clients have company id
                #betatests, demos, onsitesupports have company id
     
        def genProgrammers(self):
                for i in range(self.iteration*self.N_programmers, (self.iteration+1)*self.N_programmers):
                        p = Programmer(first_name="fp"+str(i), last_name="lp"+str(i), years_of_experience=(i % 11)+1, company_id=random.randint(1, self.N_companies))
                        self.session.add(p)
                self.session.commit()
                #projects has programmer list
                #onsitesupports has programmerlist

        def genClients(self):
                companies = self.session.query(Company)
                cs = random.sample(list(companies), random.randint(0, 6))
                for i in range(self.iteration*self.N_clients, (self.iteration+1)*self.N_clients):
                        c = Client(first_name="fc"+str(i), last_name="lc"+str(i), companies=cs)
                        self.session.add(c)
                self.session.commit()
                #betatests has client list
                #demos has client list

        def genSalespeople(self):
                for i in range(self.iteration*self.N_salesperson, (self.iteration+1)*self.N_salesperson):
                        s = Salesperson(first_name="fs"+str(i), last_name="ls"+str(i), trustworthy=bool(random.getrandbits(1)))
                        self.session.add(s)
                self.session.commit()
                #demos has salespeople list

        def genUsers(self):
                for i in range(self.iteration*self.N_users, (self.iteration+1)*self.N_users):
                        u = User_p(first_name="fs"+str(i), last_name="ls"+str(i), age=random.randint(5, 99))
                        self.session.add(u)
                self.session.commit()
                #projects has users list
                #betatests has users list

        def genProjects(self):
                for i in range(self.iteration*self.N_projects, (self.iteration+1)*self.N_projects):
                        company=random.randint(1, (self.iteration+1)*self.N_companies)
                        companies = list(self.session.query(Company))
                        programmers = companies[company-1].programmers

                        if(len(programmers)==0):
                                project_programmers = []
                        else:
                                num_programmers = len(programmers)+1
                                while num_programmers > len(programmers):
                                        num_programmers = random.randint(1, 10)
                                project_programmers = random.sample(programmers, num_programmers)

                        us = random.sample(list(self.session.query(User_p)), random.randint(0, 500))
                      
                        languages=["Java", "Python", "Go", "Rust"]
                        lang = languages[random.randint(0, len(languages)-1)]
        
                        p = Project(programmers=project_programmers, users=us, language=lang, in_production=bool(random.getrandbits(1)),
                         description="project"+str(i), company_id=company)
                        self.session.add(p)
                self.session.commit()
                #betatests, demos, onsitesupports have lists


        def genBetaTests(self):
                for i in range(self.iteration*self.N_betatests, (self.iteration+1)*self.N_betatests):
                        project=random.randint(1, (self.iteration+1)*self.N_projects)
                        projects = list(self.session.query(Project))
                        p = projects[project-1]
                        company = p.company_id

                        users = list(p.users)
                        if(len(users)==0):
                                us = []
                        else:
                                num_users = random.randint(0, len(users)-1)
                                us = random.sample(users, num_users)

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
                for i in range(self.iteration*self.N_demos, (self.iteration+1)*self.N_demos):
                        project=random.randint(1, (self.iteration+1)*self.N_projects)
                        projects = list(self.session.query(Project))
                        p = projects[project-1]
                        company = p.company_id

                        companies = list(self.session.query(Company))
                        clients = companies[company-1].clients
                        if(len(clients)==0):
                                cs = []
                        else:
                                num_clients = random.randint(0, len(clients)-1)
                                cs = random.sample(clients, num_clients)

                        salespeople = list(self.session.query(Salesperson))
                        if(len(salespeople)==0):
                                sp = []
                        else:
                                num_salespeople = random.randint(0, len(salespeople)-1)
                                sp = random.sample(salespeople, num_salespeople)

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
                for i in range(self.iteration*self.N_onsitesupports, (self.iteration+1)*self.N_onsitesupports):
                        project=random.randint(1, (self.iteration+1)*self.N_projects)
                        projects = list(self.session.query(Project))
                        p = projects[project-1]
                        company = p.company_id

                        programmers = p.programmers
                        if(len(programmers)==0):
                                ps = []
                        else:
                                num_programmers = random.randint(0, len(programmers)-1)
                                ps = random.sample(programmers, num_programmers)

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
           