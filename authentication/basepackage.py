import smtplib
import random
import sqlite3


class generate_otp:
    def send_otp(self,receiver):
        try:
          OTP=random.randint(1000,9999)
          content='''Subject:Verification Code For Account Creation
          \nDear user, we received a request for account creation with your email in Fitness Dev-Love-Per Web application\n 
          Your Email Verification code is '''+str(OTP)+'''\n\nIf this action is not initiated by you, you can safely discard this email'''
          server=smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login('fitnessdevloveper@gmail.com','ihdcwjkwsboiqwjv')
          server.sendmail('fitnessdevloveper@gmail.com',receiver,content)
          return OTP
        except Exception as e:
            print(e)
            return 1
        #    print("error occured while sending OTP")
class connect_backend():
    def __init__(self):
        try:
           self.connection=sqlite3.connect("main_db.db")
           self.cursor=self.connection.cursor()
           self.cursor.execute('''CREATE TABLE  IF NOT EXISTS USER_DATA(username sting,password string)''')
        except:
            print('error occured while establishing connection with database')
    def insert_user_data(self,data):
        tuplee=(data['user_name'],data['password'])
        insert_query="INSERT INTO USER_DATA VALUES"+str(tuplee)
        self.cursor.execute(insert_query)
        self.connection.commit()
        return 0
    def retrieve_data(self):
        self.cursor.execute('''SELECT * FROM USER_DATA''')
        present_users_data=self.cursor.fetchall()
        return present_users_data#returns list of tuples
    #connection should be closed all activities