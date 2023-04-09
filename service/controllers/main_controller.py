from flask import render_template, request, Response, redirect, url_for 
from service.controllers import bp_main as main

# ~/main/
@main.route("/")
def home():
    return render_template("main/index.html")