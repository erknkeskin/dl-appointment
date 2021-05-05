from controller.auth import bp_auth
from controller.dashboard import bp_dashboard
from controller.appointment import bp_appointment

from app import *

app.register_blueprint(bp_auth)
app.register_blueprint(bp_dashboard)
app.register_blueprint(bp_appointment)

if __name__ == "main":
    app.run()
