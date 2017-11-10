from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=OUxIy0hwIPwpys8dzkVjUXJW5SOVYcsN6ofZkyvY")
    data = u.read()
    j = json.loads(data)
    return render_template("nasa.html", img = j["hdurl"], title = j["title"], date = j["date"], explanation = j["explanation"], rights = j["copyright"])

if __name__ == "__main__":
    app.debug = True
    app.run()

