from flask import Flask, render_template

app = Flask(__name__)

# --- DATA HELPERS ---
def get_sensor_data():
    """Returns data for the Doughnut Chart in the Dashboard"""
    return {
        "labels": ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"],
        "amounts": [1200, 1900, 3000, 2500, 2200, 4100]
    }

def get_my_projects():
    """Returns the list of projects for the Portfolio"""
    return [
        {
            "title": "Gylsmix Control Panel", 
            "desc": "A high-performance dashboard featuring glassmorphism and real-time Chart.js telemetry.", 
            "tag": "Data Viz"
        },
        {
            "title": "Neural Gateway", 
            "desc": "A centralized entry point for web modules using Flask routing and custom CSS effects.", 
            "tag": "Backend"
        },
        {
            "title": "Crypto Tracker", 
            "desc": "Experimental project for monitoring blockchain frequency and market trends.", 
            "tag": "Web3"
        }
    ]

# --- ROUTES ---

@app.route('/')
def index():
    """The Main Selection Screen (Gateway)"""
    return render_template('choice.html')

@app.route('/dashboard')
def dashboard():
    """The Control Panel with Chart.js Doughnut Chart"""
    data = get_sensor_data()
    return render_template('index.html', sensor_data=data)

@app.route('/portfolio')
def portfolio():
    """The Portfolio Showcase with Jinja2 Loops"""
    projects_list = get_my_projects()
    return render_template('portfolio.html', projects=projects_list)

# --- ERROR HANDLING ---
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404: Module Not Found</h1><p>The system could not locate the requested route.</p>", 404

# --- RUN THE SYSTEM ---
if __name__ == '__main__':
    # host='0.0.0.0' is the key to making it work on your Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True)