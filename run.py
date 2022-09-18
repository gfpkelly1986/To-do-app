import os
from taskmanager import app

# __name__ wil be == __main__ if its is the route access to 
# the application
# if this file was imported, name would == taskmanager.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
