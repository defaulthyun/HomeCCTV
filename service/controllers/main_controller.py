import os

# py을 모듈가져 온 후, (객체)를 세팅해서 처리 가능
import service.config as config
from flask import render_template, request, session, Response, redirect, url_for, g
from service.controllers import bp_main as main

# ~/main/
@main.route("/")
def home():
    return render_template("main/index.html")