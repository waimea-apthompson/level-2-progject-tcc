#===========================================================
# level-2-progject-tcc
# By austin thompson
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/")
def show_bookings():
    with connect_db() as db:
        sql = """
            SELECT id, id, name, phone_number
            FROM bookings
            ORDER BY ASC
        """
        params = ()
        notes = db.execute(sql, params).fetchall()

        return render_template("pages/tcc.jinja", notes=notes)



#-----------------------------------------------------------
# handle the creature from data
#-----------------------------------------------------------
@app.post("/presnol info/new")
def process_presnol_info_form():
    name = request.form.get("name", "unknown").strip()
    what_they_getting = request.form.get("what_they_getting", "unknown").strip()
    phone_number= request.form.get("phone_number", "unknown").strip()

#connect to the db
    with connect_db() as db:

        sql = """
            INSERT INTO presnol info (name, phone_number, what_they_getting)
            VALUES (?, ?)

        """
        params = (name, phone_number, what_they_getting)

    #run the query
        db.execute(sql,params)

        flash(f"presnol info {name} added successfully")

    return redirect("/")


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

