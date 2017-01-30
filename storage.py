from interfaces import IStorage
from zope.interface import implementer
from zope.component import getGlobalSiteManager
import psycopg2

@implementer(IStorage)
class PostgreSQLStorage(object):
    def __init__(self,
            user,
            password,
            host="172.16.19.20",
            db="vechicle"):
        self.user=user
        self.password=password
        self.host=host
        self.db=db
        self.connect()
    def connect(self):
        self.conn = psycopg2.connect("""
            dbname={}
            user={}
            password={}
            port={}
            host={}
        """.format(self.db, self.user, self.password,
            15432, self.host))

# FIXME: Add cofiguration via .ini-file
conn=PostgreSQLStorage(user="postgres",password="vechicles")

GSM=getGlobalSiteManager()
GSM.registerUtility(conn, name="vechicle")

