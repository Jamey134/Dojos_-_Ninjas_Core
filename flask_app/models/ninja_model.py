from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
        DB = "dojos_and_ninjas_schema"

        def __init__(self, data):
                self.id = data['id']
                self.first_name = data['first_name']
                self.last_name = data['last_name']
                self.age = data['age']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']
                self.dojo_id = data['dojo_id']


        @classmethod
        def get_all(cls):
                query = "SELECT * FROM ninjas;"
                results = connectToMySQL(cls.DB).query_db(query)
                ninjas = []
                for n in results:
                        ninjas.append(cls(n))
                return ninjas



        @classmethod  # <========CREATE FUNCTION
        def create(cls, data):
                ninjaCount= len(Ninja.get_all()) + 1
                data = data.to_dict()
                data['id'] = ninjaCount
                print(f"\n newID: {ninjaCount} \n")
                query = """

                INSERT INTO ninjas (id, first_name, last_name, age, dojos_id)
                VALUES (`%(id)s`,`%(first_name)s`,`%(last_name)s`,`%(age)s`,`%(dojos)s`;

                """
                # make sure to call the connectToMySQL function with the schema you are targeting.
                results = connectToMySQL(cls.DB).query_db(query, data)
                return results


        @classmethod  # <----- EDIT VALUES
        def get_one(cls, data):
                query = """
                SELECT * FROM ninjas
                WHERE id = %(id)s ;
                        """
                results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

                return cls(results[0])


        @classmethod  # <------- UPDATE
        def update(cls, data):
                query = """
                UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s, age=%(age)s
                WHERE id = %(id)s
                        """
                results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
                return results


        @classmethod  # <------- DELETE
        def delete(cls, data):
                query = """
                DELETE FROM users 
                WHERE ID = %(id)s ;
                """

                results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

                return results


        @classmethod  # <---- SHOW USERS
        def show(cls, data):
                query = """ 
                SELECT * FROM users
                """
