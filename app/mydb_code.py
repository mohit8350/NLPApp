import json
class Database:

    def adddata(self, name, email, password):
        with open('mydb.json', 'r') as rf:
            database = json.load(rf)
        
        if email in database:
            return False
        else:
            database[email] = name, password
            with open('mydb.json', 'w') as wf:
                json.dump(database, wf)
            return True
        
    def search(self,email,password):
        with open('mydb.json','r') as rf:
            database = json.load(rf)
        
        if email in database:
            if database[email][1] == password:
                return True
            else:
                return False
        else:
            return False