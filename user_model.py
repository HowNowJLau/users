from mysqlconnection import connectToMySQL

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
    def create(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)
        """
        return connectToMySQL('users_schema').query_db(query, data)
