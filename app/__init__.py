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
# Welcome page
#-----------------------------------------------------------
@app.get("/")
def new_booking():
    #connect to the db
    with connect_db() as db:
        sql = """
                SELECT id, name
                FROM people
                ORDER BY name ASC
            """
            #run the query
        params = ()
        people = db.execute(sql, params).fetchall()    
    return render_template("pages/cust_form.jinja", people=people)
    

#-----------------------------------------------------------
# new opintment
#-----------------------------------------------------------
@app.get("/tcc_list")
def show_tcc_list():
    #connect to the db
    with connect_db() as db:
        sql = """
                SELECT

                    people.id   AS p_id, 
                    bookings.id AS b_id, 
                    people.name, 
                    bookings.treatment, 
                    people.phone, 
                    bookings.time

                    FROM people
                    JOIN bookings ON bookings.person_id = people.id
                    ORDER BY bookings.time ASC
            """
            #run the query
        params = ()
        bookings = db.execute(sql, params).fetchall()

    return render_template("pages/tcc_list.jinja", bookings=bookings)



#-----------------------------------------------------------
# handle the existing cust from data
#-----------------------------------------------------------
@app.post("/cust/current")
def process_existing_cust_form():
    person_id = request.form.get("person_id", 0)

#connect to the db
    with connect_db() as db:
        #geting a old costmer from there id 
        sql = """
                SELECT name
                FROM people
                WHERE id=?
            """
            #run the query
        params = (person_id,)
        person = db.execute(sql, params).fetchone()

    return render_template("pages/tcc_form.jinja", person_id=person_id, person_name=person["name"])


#-----------------------------------------------------------
# handle the treatment booking from data
#-----------------------------------------------------------
@app.post("/treatment/new")
def process_treatment_form():
    person_id = request.form.get("cust_id", 0)
    time = request.form.get("time", "unknown").strip()
    treatment = request.form.get("treatment", "unknown").strip()
    #connect to the db
    with connect_db() as db:
        sql = """
                INSERT INTO bookings (person_id, time, treatment)
                VALUES (?, ?, ?)
                
            """
            #run the query
        params = (person_id, time, treatment)
        db.execute(sql, params)

        flash("Appointment made", "success")

    return redirect("/tcc_list")


#-----------------------------------------------------------
# handle the new cust from data
#-----------------------------------------------------------
@app.post("/cust/new")
def process_new_cust_form():
    name = request.form.get("name", "unknown").strip()
    phone = request.form.get("phone", "unknown").strip()

#connect to the db
    with connect_db() as db:

        sql = """
            INSERT INTO people (name, phone)
            VALUES (?, ?)

        """
        params = (name, phone)

    #run the query
        result = db.execute(sql,params)
        person_id = result.lastrowid

        flash(f"{name} added to our system successfully")

    return render_template("pages/tcc_form.jinja", person_id=person_id, person_name=name)


#-----------------------------------------------------------
# handle the tcc from data
#-----------------------------------------------------------
@app.post("/tcc/new")
def process_tcc_form():
    time = request.form.get("time", "unknown").strip()
    name = request.form.get("name", "unknown").strip()
    phone = request.form.get("phone", "unknown").strip()
    date = request.form.get("date", "unknown").strip()
    treatment = request.form.get("treatment", "unknown").strip()

#connect to the db
    with connect_db() as db:

        sql = """
            INSERT INTO bookings (time, name, phone, date, treatment)
            VALUES (?, ?, ?, ?, ?)

        """
        params = (time, name, phone, date, treatment)

    #run the query
        db.execute(sql,params)

        flash(f"appointment for {name} added successfully")

    return redirect("/tcc_list")



#-----------------------------------------------------------
# opintment deletson- delate opintment via id
#-----------------------------------------------------------
@app.get("/booking/<int:id>/delete")
def delete_a_bookings(id):

    #connect to the db
    with connect_db() as db:
        # delete the opintment using its id
        sql = """
            DELETE FROM bookings
            WHERE id=?
        """
        #run the query
        params = (id,)
        db.execute(sql, params)

# back to list
        flash("booking deleted", "success")
        return redirect("/tcc_list")



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

