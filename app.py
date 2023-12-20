from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
clickedPoints = []
clickedPoints1 = []

# Variables to store (x_min, x_max) and (y_min, y_max) for clickedPoints
x_range_points = {'min': None, 'max': None}
y_range_points = {'min': None, 'max': None}

# Variables to store (x_min, x_max) and (y_min, y_max) for clickedPoints1
x_range_points1 = {'min': None, 'max': None}
y_range_points1 = {'min': None, 'max': None}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_name = request.form['video_name']
        return render_template('play.html', video_name=video_name)
    return render_template('index.html')

@app.route('/save_coordinates', methods=['POST'])
def save_coordinates():
    global clickedPoints, clickedPoints1, x_range_points, y_range_points, x_range_points1, y_range_points1
    data = request.get_json()
    clickedPoints = data.get('clickedPoints', [])
    clickedPoints1 = data.get('clickedPoints1', [])

    update_range_values(clickedPoints, x_range_points, y_range_points)
    update_range_values(clickedPoints1, x_range_points1, y_range_points1)

    return jsonify({'success': True})

@app.route('/view_coordinates', methods=['GET'])
def view_coordinates():
    global x_range_points, y_range_points, x_range_points1, y_range_points1
    return jsonify({
        'x_range_points': x_range_points,
        'y_range_points': y_range_points,
        'x_range_points1': x_range_points1,
        'y_range_points1': y_range_points1
    })

def update_range_values(points, x_range, y_range):
    x_values = [point['x'] for point in points]
    y_values = [point['y'] for point in points]

    x_range['min'] = min(x_values) if x_values else None
    x_range['max'] = max(x_values) if x_values else None
    y_range['min'] = min(y_values) if y_values else None
    y_range['max'] = max(y_values) if y_values else None

if __name__ == '__main__':
    app.run(debug=True)
