
import mysql.connector
from tkinter import messagebox
class DBhelper:
    def __init__(self):
        try:
              self._connection=mysql.connector.connect(host="remotemysql.com", user="eULkE4oaue", password="56pJskwG6X", database="eULkE4oaue")
              self._mycursor=self._connection.cursor()
        except:
              self.errorMessage("Error","Could Not Connect Try again")
    def search(self,key1,value1,key2,value2,table):
        query="SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'".format(table,key1,value1,key2,value2)


        self._mycursor.execute(query)
        response=self._mycursor.fetchall()


        return response
    def search2(self,key1,value1,table):
        query = "SELECT * FROM `{}` WHERE `{}` LIKE '{}'".format(table, key1, value1)

        self._mycursor.execute(query)
        response = self._mycursor.fetchall()

        return response
    def searchone(self,key1,value1,table,type):
        query="SELECT * FROM `{}` WHERE `{}` {} '{}'".format(table,key1,type,value1)

        self._mycursor.execute(query)
        response=self._mycursor.fetchall()

        return response
    def insert(self,mydict,table):
        cols='user_id'+','+""
        vals='NULL'+','+""
        for i in mydict:
            cols = cols + "`" + i + "`" + ","
            vals = vals + "'" + str(mydict[i]) + "'" + ","
        cols=cols[:-1]
        vals=vals[:-1]
        query="INSERT INTO `{}`({}) VALUES ({})".format(table,cols,vals)


        try:
            self._mycursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0
    def update(self,session,name,email,password,age,bg,gender,city,bio):
        query="UPDATE `usersactual` SET `name`='{}',`email`='{}',`password`='{}',`age`='{}',`bg`='{}',`gender`='{}',`city`='{}',`bio`='{}' WHERE user_id={}".format(name,email,password,age,bg,gender,city,bio,session)

        try:
            self._mycursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0

    def insert2(self, mydict, table):
            cols = 'proposal_id' + ',' + ""
            vals = 'NULL' + ',' + ""
            for i in mydict:
                cols = cols + "`" + i + "`" + ","
                vals = vals + "'" + str(mydict[i]) + "'" + ","
            cols = cols[:-1]
            vals = vals[:-1]
            query = "INSERT INTO `{}`({}) VALUES ({})".format(table, cols, vals)


            try:
                self._mycursor.execute(query)
                self._connection.commit()
                return 1
            except:
                return 0

    def errorMessage(self, title, message):
        messagebox.showerror(title, message)