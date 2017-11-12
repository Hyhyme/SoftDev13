from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
    
    nasa = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=OUxIy0hwIPwpys8dzkVjUXJW5SOVYcsN6ofZkyvY")
    picOfDay = nasa.read()
    cool = json.loads(picOfDay)

    #change these to calculate something else! Note the url-encoded " ^ "
    op = "factor"
    ex = "x%5E2 - 1"
    
    newton = urllib2.urlopen("https://newton.now.sh/" + op + "/" + ex)
    calc = newton.read()
    j = json.loads(calc)

    return render_template("thing.html", img = cool["hdurl"], title = cool["title"], date = cool["date"], explanation = cool["explanation"], rights = cool["copyright"], operation = j["operation"], expression = j["expression"], result = j["result"])

if __name__ == "__main__":
    app.debug = True
    app.run()

