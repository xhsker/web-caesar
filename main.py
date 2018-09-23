

from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

alpha_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin:10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/encrypt" method="POST">
        <div>
            <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value='0'/>
        </div>
            <textarea type="text" name="text"></textarea>
            <br>
            <input type="submit"/>
        </label>
    </body>
</html>
"""

@app.route("/")
def index():
    return alpha_form


@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = rot
    text = rotate_string
    answer = request.form["text"]
    return "The answer is:"+answer

app.run()


