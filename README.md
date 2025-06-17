# Background Removal API

A simple and efficient API to remove backgrounds from images, built with Flask and the rembg library.

## Features

- Remove backgrounds from uploaded images
- Returns transparent PNG images
- Simple REST API interface
- Ready for deployment to platforms like Heroku

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd removebg
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python remove_bg.py
   ```

The API will be available at `http://localhost:5000`.

## API Endpoints

### Test Endpoint

```
GET /test
```

Use this endpoint to check if the API is running correctly.

**Response:**
```json
{
  "status": "success",
  "message": "Background removal API is running correctly",
  "endpoints": {
    "test": "/test [GET]",
    "remove-background": "/remove-bg [POST]"
  }
}
```

### Background Removal Endpoint

```
POST /remove-bg
```

Upload an image to have its background removed.

**Parameters:**
- `image`: The image file to process (form-data)

**Response:**
- A PNG image with transparent background where the background has been removed
- Content-Type: `image/png`
- File name: `removed_background.png`

**Error Responses:**
- 400: When no image is provided or the image is empty
- 500: When an error occurs during image processing

## Example Usage

### Using cURL

```bash
curl -X POST -F "image=@/path/to/your/image.jpg" -o "output.png" http://localhost:5000/remove-bg
```

### Using Python Requests

```python
import requests

url = "http://localhost:5000/remove-bg"
files = {"image": open("image.jpg", "rb")}
response = requests.post(url, files=files)

if response.status_code == 200:
    with open("removed_background.png", "wb") as f:
        f.write(response.content)
    print("Background removed successfully!")
else:
    print(f"Error: {response.json()}")
```

## Dependencies

- Flask: Web framework
- rembg: Background removal library
- Pillow: Image processing
- onnxruntime: Required by rembg for neural network operations
- gunicorn: Production web server
