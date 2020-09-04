import app from app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'