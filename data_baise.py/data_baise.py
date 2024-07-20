
# 117
# ------------------------
# -- Databases => Intro --
# ------------------------
# - Database Is A Place Where We Can Store Data
# - Database Organized Into Tables (Users, Categories)
# - Tables Has Columns (ID, Username, Password)
# - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# - SQL Stand For Structured Query Language
# - SQLite => Can Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# - Data Inside Database Has Types (Text, Integer, Date)
# ------------------------------------------------------










# 118
# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Create The Tables and Fields
db.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")

# Close Database
db.close()



