import json
import pydgraph
import time


queries = [
"""{
query1(func: allofterms(first_name, "fp210")) {
        works_for { name }
        }
}""",
"""{
query2(func: allofterms(name, "C80")) {
        ~works_for { first_name }
	}
}""",
"""{
query3(func: eq(count(~works_for), 3)) {
	companies: count(uid)
        }
}""",
"""{
var(func: has(headed_by)) {
	num_employees as count(~works_for)
}
  
query4(func: uid(num_employees), orderdesc: val(num_employees), first: 1) {
	name
	count(~works_for)
	}
}""",
"""{
query5(func: allofterms(language, "Python")) @normalize {
  ~provided_for {
	managed_by @filter (gt(years_of_experience, 3)) {
	first_name: first_name
        last_name: last_name
	        }	
        }
}
}""",
"""{
query6(func: uid(0x1bef)) {
  	first_name
	~attends {
		demoing @filter (allofterms(language, "Rust")) {
			uid
    			description
			}
		}
}
}""",
"""{
query7(func: uid(0x2ae)) @cascade @normalize {
        ~belongs_to @filter (eq(in_production, true)) {
		project: description
        }
}
}""",
"""{ 
var(func: has(belongs_to)) @filter (allofterms(language, "Rust")) {
	rust_demos as ~demoing
}
  
var(func: has(trustworthy)) @filter (eq(trustworthy, true)) {
	~presented_by {
		good_rust_demos as demoing @filter (uid(rust_demos))
  }
}
  
query8(func: uid(good_rust_demos)) {
		count(~attends)
  }
}""",
"""{
query9(func: allofterms(name, "C492")) @cascade @normalize {
		~belongs_to @filter (allofterms(language, "Rust")) {
      		count(~provided_for)
			~provided_for {
				managed_by {
					first_name: first_name
				}
			}
		}
	}

}""",
"""{
query10(func: uid(0x21c8)) @cascade {
        count(designed_for)
}
}""", 
"""{
query11(func: uid(0xd17)) {
        ~designed_for {
		description
        }
}
}""", 
"""{     
var(func: has(headed_by)) {
	dim_projects as ~belongs_to @filter (anyofterms(language, "Java Python") and eq(in_production, true))
}
    
query12(func: has(handled_by)) @filter (gt(count(managed_by), 2)) {
	provided_for @filter (uid(dim_projects)) {
		description
  }
  }
}"""

]



client_stub = pydgraph.DgraphClientStub('localhost:9080')

client = pydgraph.DgraphClient(client_stub)


times = []
n_repeats = 100
for query in queries:
        print(query)
        total = 0
        for _ in range(n_repeats):
                # Best-effort queries are faster than normal queries because they bypass the normal consensus protocol. For this same reason, best-effort queries cannot guarantee to return the latest data. Best-effort queries are only supported by read-only transactions.
                # txn(read_only=True, best_effort=True)
                txn = client.txn(read_only=True)
                try:
                        start = time.time()
                        res = txn.query(query)
                        end = time.time()
                        total+=(end - start)
                        # print('Response: {}'.format(json.loads(res.json)))
                except pydgraph.AbortedError:
                        print("error")
                finally:
                        txn.discard()
        times.append(total*1000/n_repeats)
i = 1
for t in times:
        print("query", i, t)
        i+=1