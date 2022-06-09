import json

objList = []
with open('csv/ten_k_db.json') as f:
    for jsonObj in f:
        dj = json.loads(jsonObj)
        d = dj
        if(dj['type'] == "node"):
                d['type'] = dj['labels'][0]
        if(dj['type'] == "relationship"):
                d = {"uid": dj['start']['id'], dj['label']: {"uid": dj['end']['id']}}
        objList.append(d)
with open("preprocessed_2.json", "w") as outfile:
        json.dump(objList, outfile)


