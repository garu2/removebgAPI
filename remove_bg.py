import io
import os
from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'status': 'success',
        'message': 'Background removal API is running correctly',
        'endpoints': {
            'test': '/test [GET]',
            'remove-background': '/remove-bg [POST]'
        }
    })

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    # Check if image file is present in request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file in request'}), 400
        
    file = request.files['image']
    
    # If user does not select file
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
        
    # Process the image
    try:
        # Read image
        img = Image.open(file.stream)
        
        # Remove background
        output = remove(img)
        
        # Save to BytesIO object
        img_byte_arr = io.BytesIO()
        output.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # Return the processed image
        return send_file(
            img_byte_arr,
            mimetype='image/png',
            as_attachment=True,
            download_name='removed_background.png'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Host='0.0.0.0' makes the server publicly available
    app.run(host='0.0.0.0', port=port, debug=False)