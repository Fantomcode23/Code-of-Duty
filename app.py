from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

app = Flask(__name__)

# Load the YOLO model
model = YOLO('best2.pt')

# Brand dictionary
brand_dict = {
    'Peter England': [41.4, 43.2, 45.2, 47.2],
    'Louis Philippe': [44.45, 45.72, 46.99, 48.26],
    'Raymonds': [40, 42, 44, 46],
    'Teamspirit': [36, 38, 40, 42],
    'Denims': [38, 41, 44, 47]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image:
        image_path = 'temp_image.jpg'
        image.save(image_path)

        try:
            results = model.predict(image_path, save=True, imgsz=320, conf=0.5)
            keypoints = results[0].keypoints.xy[0]
            
            b, c = keypoints[1][0], keypoints[1][1]
            d, e = keypoints[2][0], keypoints[2][1]
            f, g = keypoints[3][0], keypoints[3][1]
            h, i = keypoints[4][0], keypoints[4][1]

            hips = (((b-d)*2) + ((c-e)*2))**(1/2)
            waist = (((f-h)*2) + ((g-i)*2))**(1/2)
            height = float(results[0].boxes.xywh[0][3])

            os.remove(image_path)

            return jsonify({'hips': float(hips), 'waist': float(waist), 'image_height': float(height)})
        except Exception as e:
            os.remove(image_path)
            return jsonify({'error': str(e)}), 500

@app.route('/calculate_size', methods=['POST'])
def calculate_size():
    data = request.json
    real_height = float(data['height'])
    hips = float(data['hips'])
    waist = float(data['waist'])
    image_height = float(data['image_height'])

    hips_cm = (real_height / image_height) * hips + 3
    waist_cm = (real_height / image_height) * waist

    sizes = {}
    for brand, measurements in brand_dict.items():
        if hips_cm <= measurements[0]:
            sizes[brand] = "SMALL"
        elif measurements[0] < hips_cm <= measurements[1]:
            sizes[brand] = "MEDIUM"
        elif measurements[1] < hips_cm <= measurements[2]:
            sizes[brand] = "LARGE"
        elif measurements[2] < hips_cm <= measurements[3]:
            sizes[brand] = "EXTRA LARGE"
        else:
            sizes[brand] = "EXTRA EXTRA LARGE"

    return jsonify(sizes)

@app.route('/redirect_to_shopping', methods=['POST'])
def redirect_to_shopping():
    data = request.json
    brand = data['brand']
    size = data['size']

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.amazon.com")
        time.sleep(5)

        search_bar = driver.find_element("name", "field-keywords")
        search_query = f"Size {size} tshirt in {brand}"
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)

        time.sleep(5)
        current_url = driver.current_url
    finally:
        driver.quit()

    return jsonify({'url': current_url})

if __name__ == '__main__':
    app.run(debug=True)