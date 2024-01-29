# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g, jsonify

app = Flask("login")

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "login.db")


# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    conn = getattr(g, "_database", None)
    if conn is None:
        conn = g._database = sqlite3.connect(DATABASE)
    return conn


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    # 这里应该加入密码散列的步骤
    # 这里添加验证用户逻辑
    # 如果验证成功，存储用户信息
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return jsonify({'message': 'User logged in successfully'})
    except sqlite3.Error as error:
        print("Error while inserting into SQLite table", error)
        return jsonify({'error': str(error)})
    finally:
        if conn:
            conn.close()
    
    return redirect(url_for('success'))

@login.route('/success')
def success():
    return 'User registered successfully'

if __name__ == '__main__':
    app.run(debug=True)
