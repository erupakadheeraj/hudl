import flask, urllib, hashlib, re
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template("404.html")



# A route to return all of the available entries in our catalog.
@app.route('/<path:text>', methods=['GET'])
def api_all(text):
  if re.match("^avatar/[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", text):
    path,email = text.split("/")
    email = email.encode(encoding = 'UTF-8',errors = 'strict')
    default = 'https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50'
    size = 80
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.parse.urlencode({'d':default, 's':str(size)})
    return render_template("index.html", user_image = gravatar_url)
  else:
    return render_template("404.html")

if (__name__ == '__main__'):
  app.run()