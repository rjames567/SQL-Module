# ------------------------------------------------------------------------------
# This file handles the creation and deletion of databases, including creating
# and dropping tables
#
# Each database:
#     Table names
#     Audit trails
#     Table names
#     Database name
#     Database meta information
#     Table data
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Standard Python library imports
# ------------------------------------------------------------------------------
import os
import datetime

# ------------------------------------------------------------------------------
# Create a database
# ------------------------------------------------------------------------------
def create_database(database_name: str):
    filepath = "." + database_name
    os.mkdir(filepath)
    filepath += "/"

    with open(filepath + "db.meta", "w+") as f:
        f.write(database_name + "\n")  # Database name
        f.write(datetime.datetime.now().strftime("%d,%m,%Y,%H,%M,%S"))  # Date created
