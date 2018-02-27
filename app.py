import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mon

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def hello():
    return render_template("hi.html")

@app.route("/display", methods=["GET","POST"])
def submit():
    if( request.args["name"] ):
        print request.args["name"]
        stuff = mon.findName(request.args["name"])
        for x in stuff:
            flash(x)
                
    elif( request.args["id"] ):
        stuff = mon.findId(request.args["id"])
        for x in stuff:
            flash(x)

               
    elif( request.args["yr"] ):
        print request.args["yr"]
        stuff = mon.findYear(request.args["yr"])
        for x in stuff:
            flash(x)
            
    elif( request.args["mass"] and request.args["year"] ):
        stuff = mon.my(request.args["mass"],request.args["year"])
        for x in stuff:
            flash(x)

    elif( request.args["minMass"] and request.args["maxMass"] ):
        stuff = mon.massRange(request.args["minMass"],request.args["maxMass"])
        for x in stuff:
            flash(x)
    else:
        flash("huh")
    return render_template("hi.html",stuff=stuff)


if __name__ == '__main__':
    app.debug = True
    app.run()
