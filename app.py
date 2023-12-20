from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
clickedPoints = []
clickedPoints1 = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_name = request.form['video_name']
        return render_template('play.html', video_name=video_name)
    return render_template('index.html')

@app.route('/save_coordinates', methods=['POST'])
def save_coordinates():
    global clickedPoints, clickedPoints1
    data = request.get_json()
    clickedPoints = data.get('clickedPoints', [])
    clickedPoints1 = data.get('clickedPoints1', [])
    
    check_and_process_data()  # Xử lý dữ liệu khi cả hai mảng đều đủ giá trị

    return jsonify({'success': True})

@app.route('/view_coordinates', methods=['GET'])
def view_coordinates():
    global clickedPoints, clickedPoints1
    return jsonify({'clickedPoints': clickedPoints, 'clickedPoints1': clickedPoints1})

def check_and_process_data():
    global clickedPoints, clickedPoints1
    if len(clickedPoints) == 4 and len(clickedPoints1) == 4:
        # Xử lý dữ liệu theo nhu cầu của bạn
        # Ví dụ: In ra console
        print("Clicked Points:", clickedPoints)
        print("Clicked Points 1:", clickedPoints1)

if __name__ == '__main__':
    app.run(debug=True)
