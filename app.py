from flask import Flask, render_template
import os
from werkzeug.middleware.proxy_fix import ProxyFix

# Create Flask application
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Apply the proxy fix for proper IP handling behind a proxy/load balancer
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

# Import image blueprint
from image_service import image_bp

# Register blueprints
app.register_blueprint(image_bp)

# Main route (previously in frontpage.py)
@app.route('/')
def index():
    return render_template('index.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

@app.errorhandler(500)
def server_error(e):
    return "500 Internal Server Error", 500

if __name__ == '__main__':
    # Get port from environment variable for production deployments
    port = int(os.environ.get('PORT', 5000))
    
    # In production, don't run with debug mode
    debug_mode = os.environ.get('FLASK_ENV', 'production') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)