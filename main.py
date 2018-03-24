from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method='post'>
            <label for="rot">Rotate by</label>
            <input type="text" name="rot"><br>
            <textarea name="text"><br>
            <input type="submit">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

app.run()