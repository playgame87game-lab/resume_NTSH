
from flask import Flask, render_template

app = Flask(<h1>30923劉子謙</h1>)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competition')
def competition():
    return render_template('competition.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/club')
def club():
    return render_template('club.html')

@app.route('/electives')
def electives():
    return render_template('electives.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume - 30923劉子謙</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>30923劉子謙</h1>
    <p>歡迎瀏覽我的履歷網站！</p>
</body>
</html>
