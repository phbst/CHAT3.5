import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:8080", ""]}})     //跨域

# Secret key used to sign JWT
app.config['SECRET_KEY'] = ''             //token key//

@app.route('/', methods=['POST'])
@cross_origin()
def login():
    # 获取请求参数
    data = request.json
    user = data.get('username')
    password = data.get('password')
    rep_type=data.get('type')
    try:
        # 创建数据库连接
        db = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database=""                        //mysql//
        )

        # 执行查询语句
        if rep_type=='login':
            # 验证用户名和密码
            cursor = db.cursor()
            sql = "SELECT * FROM info WHERE username = %s AND password = %s"
            val = (user, password)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                # 生成 JWT
                payload = {'username': user, 'exp': datetime.utcnow() + timedelta(days=1)}
                token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
                db.close()
                return jsonify({'code': 1, 'token': token})
            else:
                db.close()
                return jsonify({'code': 0})
        elif rep_type=='signup':
            cursor = db.cursor()
            sql = "SELECT * FROM info WHERE username = %s"
            val = (user,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                db.close()
                return jsonify({'code': 2})
            else:
                sql = "INSERT INTO info (username, password) VALUES (%s, %s)"
                val = (user, password)
                cursor.execute(sql, val)
                db.commit()
                db.close()
                return jsonify({'code': 1})

    except mysql.connector.Error as error:
        # 打印连接失败信息
        return jsonify({'code': -1})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='')            //port//