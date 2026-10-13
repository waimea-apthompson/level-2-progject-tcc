#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------


class people_table:

    NAME = "people"

    SCHEMA = """
        CREATE TABLE people (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT NOT NULL,
            phone   TEXT NOT NULL,
            notes   TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO people (name, phone, notes)
        VALUES
            ("Ken", "1598336203", ""),
            ("Austin", "83268756129", "likes coffee"),
            ("Bob", "6254141104872", "has a nut allergy")
    """


class bookings_table:

    NAME = "bookings"

    SCHEMA = """
        CREATE TABLE bookings (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id   INTEGER NOT NULL,
            time        TEXT NOT NULL,
            treatment   TEXT NOT NULL,

            FOREIGN KEY (person_id) REFERENCES people(id)
        )
    """

    SEED_DATA = """
        INSERT INTO bookings (person_id, time, treatment)
        VALUES
            (1, "16:00", "Laser"),
            (1, "15:00", "Laser follow-up"),
            (2, "16:00", "Laser"),
            (3, "16:00", "Laser"),
            (2, "16:00", "Laser")
    """


    

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    people_table,
    bookings_table
    # Add more tables here...
]

