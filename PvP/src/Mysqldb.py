'''
Created on 19.10.2013

@author: Robo
'''
import sys

config = dict(host='localhost', user='root', passwd='',db="PVP2013")


try:
    import MySQLdb
   
    db = MySQLdb.connect(**config)
except ImportError:
    print "\nkgopendb.py error: MySQLdb module required for interactive usage\n"
    sys.exit(1)


except MySQLdb.Error, e:
    print "kgopendb.py: Couldn't open kajgps database"
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(2)

class Mysqldb:
 
    def database(self,barcode):
        self.barcode=barcode
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM product
                        WHERE id = %s""", (barcode))
        result = cursor.fetchone()
       
        print result[1] + ': ' + str(result[2]) + ' euros'