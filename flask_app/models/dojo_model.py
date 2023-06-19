from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos_and_ninjas_schema"  

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def get_all(cls, data):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos

@classmethod
def save(cls, data):
        query = """
        
        INSERT INTO dojos (first_name, last_name, email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results