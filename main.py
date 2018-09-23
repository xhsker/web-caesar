

from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

alpha_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin:10px 0;
                width: 540px;
                height: 120px;
                
            }}
        </style>
    </head>
    <body>
        <form acton="/" method="POST">
        <div>
            <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value= '0'/>
        </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit"/>
        </label>
    </body>
</html>
"""

@app.route("/")
def index():
    return alpha_form.format ("")


@app.route("/", methods=['POST'])
def encrypt(): 
    user_rot = int(request.form['rot'])
    user_text = request.form['text']
    answer = rotate_string(user_text, user_rot)
    return alpha_form.format(answer)

app.run()


