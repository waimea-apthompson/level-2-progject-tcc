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



class bookingsTable:

    NAME = "bookings"

    SCHEMA = """
        CREATE TABLE bookings (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id   INTEGER SECONDRY KEY
            name   TEXT NOT NULL,
            phone number    INT
            
        )
    """

    SEED_DATA = """
        INSERT INTO bookings (name, phone number)
        VALUES
            ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
            ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
            ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
            ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
            ("Important!",    1, "Remember to backup your database regularly.")
    """


class presnolinfoTable:

    NAME = "presnol info"

    SCHEMA = """
        CREATE TABLE presnol info (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id   INTEGER SECONDRY KEY,
            name   TEXT NOT NULL,
            phone number    INT
            
        )
    """

    SEED_DATA = """
        INSERT INTO presnol info (booking_id, name, phone number)
        VALUES
            (1  "ken", "1598336203"),
            (2, "austin", "83268756129"),
            (3, "bob", "6254141104872"),
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
    presnolinfoTable,
    bookingsTable
    # Add more tables here...
]

