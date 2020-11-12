# This is only for development.
import sys
sys.path.insert(0, "./app")
from app import app as app
app.debug=False
app.run(port=8080, host='127.0.0.1')