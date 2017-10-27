import sqlite3

#./sqlite3/mytest1.db
conn = sqlite3.connect('mytest1.db')
cursor = conn.cursor()

count = input('number:')
for index in range(0,int(count)):
    name  = '123'#input('student\'s name')
    username = '123'#input('student\'s username')
    id_num = '1'#input('student\'s id number:')
    # '''insert语句 把一个新的行插入到表中'''

    sql = ''' insert into students
                (name, username, id)
                values
                (:st_name, :st_username, :id_num)'''
    # 把数据保存到name username和 id_num中
    cursor.execute(sql,{'st_name':name, 'st_username':username, 'id_num':id_num})
    conn.commit()

# name  = '123'#input('student\'s name')
# username = '123'#input('student\'s username')
# id_num = '1'#input('student\'s id number:')
# # '''insert语句 把一个新的行插入到表中'''

# sql = ''' insert into students
#             (name, username, id)
#             values
#             (:st_name, :st_username, :id_num)'''
# # 把数据保存到name username和 id_num中
# cursor.execute(sql,{'st_name':name, 'st_username':username, 'id_num':id_num})
# conn.commit()
# cont = ('Another student? ')
cursor.close()