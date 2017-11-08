from flask import Flask, request
from caesar import rotate_string

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
                margin: 10px 0;
                width: 540px;
                heoght: 120px;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot"> Rotate by:</label>
                <input name="rot" value="0" type="text">
            </div>
            <br>
            <textarea name="text"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/",methods=["post"])
def encrypt():
    rot_value = int(request.form["rot"])
    text_string = request.form["text"]
    
    encrypted_string = rotate_string(text_string,rot_value)

    return "<h1>" + encrypted_string + "</h1>"


app.run()