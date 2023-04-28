from db import connect_db


class UserService():
    def getUsers():
        connection = connect_db()
        db = connection.cursor()
        db.execute("SELECT * FROM USERS")
        users = db.fetchall()
        db.close()
        connection.close()
        return users

    def getUserById(id):
        if type(id) not in [int]:
            try:
                id = int(id)
            except:
                return "Not Found"
        if(id <= 0):
            return "Not Found"
        try:
            connection = connect_db()
            db = connection.cursor()
            db.execute('SELECT * FROM USERS WHERE ID = {id}'.format(id = id))
            user = db.fetchall()
            db.close()
            connection.close()
            return user[0]
        except:
            return "Not Found"
        
    def deleteUserById(id):
        if type(id) not in [int]:
            try:
                id = int(id)
            except:
                return "Not Found"
        if(id <= 0):
            return "Not Found"
        connection = connect_db()
        db = connection.cursor()
        db.execute("DELETE FROM USERS WHERE id = {id} RETURNING *".format(id = id))
        connection.commit()
        user = db.fetchall()
        db.close()
        connection.close()
        return user[0]
    
    def createUser(name , password):
        if type(name) not in [str] or type(password) not in [str]:
            raise TypeError()
        connection = connect_db()
        db = connection.cursor()
        db.execute("INSERT INTO users (name , password) VALUES(%s , %s) RETURNING *", (name , password))
        connection.commit()        
        user = db.fetchall()
        db.close()
        connection.close()
        return user[0]
    
    def updateUser(name , password ,id):
        if type(name) not in [str] or type(password) not in [str]:
            raise TypeError()
        try:
            id = int(id)
        except:
            TypeError()
        connection = connect_db()
        db = connection.cursor()
        db.execute("UPDATE users set name = %s , password = %s where id = %s RETURNING *" , (name , password ,id))
        connection.commit()
        user = db.fetchall()
        db.close()
        connection.close()
        return user[0]
