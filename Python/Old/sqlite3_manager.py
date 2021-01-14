# Creator = omidnw
# Telegram Id = @sezavar110 # telegram.org
# Good Luck.

import sqlite3
class dbSql:
    class Sqlite:
        def connect(self, databasename): # databasename ; "برای متصل شدن به دیتابیس هستش."
            try:
                return sqlite3.connect(databasename)
            except sqlite3.Error as Error:
                return print(Error)
        #Table
        def createtable (self, databasename, tablename, columnname): # tablename "اسم جدول مورد نظر میشه." columnname "اسم ستون های جدول که میشه به صورت پرانتزی مثل دستور های دیتابیس استفاده کرد."
            try:
                c = self.connect(databasename)
                c.execute('CREATE TABLE {}({})'.format(tablename, columnname))
                c.commit()
                c.close()
            except sqlite3.Error as Error:
                return print(Error)
        def gettablename(self,DataBaseName): # "برای دریافت اسم جدول ها هستش."
            try:
                conn = self.connect(DataBaseName)
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                return c.execute("SELECT tbl_name FROM sqlite_master WHERE type='table'").fetchall()
            except sqlite3.Error as er:
                return print(er)
        def readtable(self,databasename,tablename): # "برای خواندن کل اطلاعات جدول هستش."
            try:
                c = self.connect(databasename)
                c.row_factory = sqlite3.Row
                cursor = c.execute('SELECT * FROM {}'.format(tablename))
                for row in cursor:
                    return list(row)
            except sqlite3.Error as er:
                return print(er)
        def deletetable(self, databasename, tablename): # "با این تابع می تونید هر جدولی یا تمام جدول هارو حذف کنید."
            try:
                c = self.connect(databasename)
                c.execute('DROP TABLE IF EXISTS {}'.format(tablename))
                c.commit()
                c.close()
            except sqlite3.Error as Error:
                return print(Error)
        #Finish Table
        #Value
        def insertvalue(self, databasename, tablename, columnname, valuename): # "برای وارد کردن مقدار هستش می تونید به صورت چند تایی با استفاده از پرانتز اطلاعات رو به چند جدول و ستون و... وارد کنید."
            try:
                c = self.connect(databasename)
                print(tablename)
                print(columnname)
                print(valuename)
                c.execute('INSERT INTO {}({}) VALUES ({})'.format(tablename, columnname, valuename))
                c.commit()
                c.close()
            except sqlite3.Error as Error:
                print(Error)
        def readonerecord(self,databasename,tablename,recordid): # "این دستور میشد داخل یک تابع جمع کرد اما ترجیحا بصورت یک تابع ساختمش."
            try:
                c = self.connect(databasename)
                c.row_factory = sqlite3.Row
                cursor = c.execute('SELECT * FROM {}'.format(tablename))
                for row in cursor:
                    return list(row[recordid])
            except sqlite3.Error as er:
                return print(er)
        def readrecord(self,databasename,table,recordid,recordname): # "این تابع برای خوندن اطلاعات هستش."
            try:
                conn = self.connect(databasename)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                return dict(c.execute('SELECT * FROM {} WHERE {}={}'.format(table,recordid,recordname)).fetchall())
            except sqlite3.Error as er:
                print(er)
        def deletevalue(self, databasename, tablename, columnname,  valuename): # "این تابع برای حذف مقادیر استفاده میشه."
            try:
                c = self.connect(databasename)
                c.execute('DELETE FROM {} WHERE {}={}'.format(tablename,columnname,"'" + valuename + "'"))
                c.commit()
                c.close()
            except sqlite3.Error as Error:
                return print(Error)
# "Coming Soon add English."