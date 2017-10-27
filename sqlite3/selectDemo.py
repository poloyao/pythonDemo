import sqlite3

#./sqlite3/mytest1.db
conn = sqlite3.connect('mytest1.db')
cursor = conn.cursor()

# 查询所有的学生表
# sql = '''select * from students'''

''' 得到数据库中的名字'''
sql = "select rowid,  username from students"

# 执行语句
results = cursor.execute(sql)

# 遍历打印输出
all_students = results.fetchall()
for student in all_students:
    print(student)