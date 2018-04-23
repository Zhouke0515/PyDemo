import pymysql

if __name__ == '__main__':
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='ams')
        # 查询
        with conn.cursor() as cursor:
            # cursor = conn.cursor(as_dict=True)
            exe = cursor.execute('select * from ams_users')
            fetch = cursor.fetchall()
            print(exe)
            print(fetch)

        # 更新
        with conn.cursor() as cursor:
            cursor.execute('update ams_users set mobile = %s, email=%s', ('111', 'aaa'))
            conn.commit()
    finally:
        conn.close()
