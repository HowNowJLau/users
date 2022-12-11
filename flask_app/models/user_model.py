from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%M %e, %Y') AS created_at, updated_at FROM users;
        """
        results = connectToMySQL('users_schema').query_db(query)
        user_list = []
        for user in results:
            user_list.append(cls(user))
        return user_list

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE id = %(id)s;
        """
        # query = """
        # SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%M %e, %Y') AS created_at, 
        # DATE_FORMAT(updated_at, '%M %e, %Y at %r') AS updated_at FROM users WHERE id = %(id)s;
        # """
        results = connectToMySQL('users_schema').query_db(query, data)
        print(results)
        if results:
            return cls(results[0])
        else:
            return False

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)
        """
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM users WHERE id = %(id)s;
        """
        return connectToMySQL('users_schema').query_db(query, data)
