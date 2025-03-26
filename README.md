# PlaceSeteli

Add a nice placeholder tonnin seteli for your web app.
_(It's like placekitten but with finnish humor)_

## How It Works

Simply include an image in your HTML with the desired width and height in the URL:

```html
<img src="https://placeseteli.netlify.app/400/200">
```

This will generate a 400×200 pixel placeholder image.

## Features

- Custom dimensions: Specify any width and height up to 2000px
- Consistent styling: All images are based on the same euro bill design
- Simple integration: Just use a simple image URL, no API keys or authentication needed
- Cached responses: Images are cached for better performance

## Examples

### Square Image (300×300)
```html
<img src="https://placeseteli.netlify.app/300/300">
```

### Wide Rectangle (600×200)
```html
<img src="https://placeseteli.netlify.app/600/200">
```

### Tall Rectangle (200×500)
```html
<img src="https://placeseteli.netlify.app/200/500">
```

### With CSS Classes
```html
<img src="https://placeseteli.netlify.app/400/300" class="img-fluid rounded">
```

## Local Development

To run this project locally:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/placeseteli.git
cd placeseteli
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`.

## Deployment

### Deploying to Netlify

1. Push your repository to GitHub
2. Connect Netlify to your GitHub repository
3. Set up the build settings as follows:
   - Build command: (leave empty or specify your build command if needed)
   - Publish directory: (leave empty or specify your publish directory if needed)
4. Add environment variables if required by your deployment

### Requirements

- Python 3.6+
- Flask
- Pillow (PIL)

## License

Free to use for personal and commercial projects.