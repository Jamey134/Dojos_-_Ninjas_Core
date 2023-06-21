from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos_and_ninjas_schema"  

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = """SELECT *
                FROM dojos
                JOIN ninjas
                ON dojos.id = ninjas.dojo_id
                WHERE ninjas.dojo_id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db( query , data )
        return results
    
    @classmethod  # <----- EDIT VALUES
    def get_one(cls, data):
            query = """
            SELECT * FROM dojos
            WHERE dojos.id = %(id)s ;
                        """
            results = connectToMySQL(cls.DB).query_db(query, data)

            one_dojo = cls(results[0])
            return one_dojo

    @classmethod
    def save(cls, data):
        query = """
        
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
