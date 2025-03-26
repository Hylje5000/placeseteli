from flask import Blueprint, send_file, abort, current_app
from PIL import Image
import io
import os
from pathlib import Path

image_bp = Blueprint('image_service', __name__)

@image_bp.route('/<int:width>/<int:height>')
def resize_image(width, height):
    # Define reasonable size limits
    max_dimension = 2000
    min_dimension = 1
    
    if width < min_dimension or height < min_dimension:
        abort(400, description="Dimensions must be positive")
    if width > max_dimension or height > max_dimension:
        abort(400, description=f"Dimensions cannot exceed {max_dimension}px")
    
    try:
        # Use a more robust path resolution method
        base_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        image_path = base_dir / 'seteli.png'
        
        # Open the image
        img = Image.open(image_path)
        
        # Resize the image with antialiasing for better quality
        img_resized = img.resize((width, height), Image.LANCZOS)
        
        # Save to a BytesIO object
        img_io = io.BytesIO()
        img_resized.save(img_io, format='PNG', optimize=True)
        img_io.seek(0)
        
        # Set cache header for 1 day (86400 seconds)
        cache_timeout = 86400
        
        # Return the image with appropriate headers
        return send_file(
            img_io, 
            mimetype='image/png',
            max_age=cache_timeout,
            etag=f"seteli-{width}x{height}",
            last_modified=os.path.getmtime(image_path)
        )
    except FileNotFoundError:
        abort(404, description="Source image not found")
    except Exception as e:
        current_app.logger.error(f"Error generating image: {str(e)}")
        abort(500, description="An error occurred while processing the image")