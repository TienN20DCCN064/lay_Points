# Import các module cần thiết từ Flask
from flask import Flask, render_template, request, jsonify

# Khởi tạo đối tượng Flask để tạo ứng dụng web
app = Flask(__name__)

# Danh sách để lưu trữ các điểm được chọn trên video. Có hai danh sách tương ứng với hai loại điểm.
clickedPoints = []
clickedPoints1 = []

# Các biến để lưu trữ giá trị min và max của tọa độ X và Y của các điểm được chọn trên video.
x_range_points = {'min': None, 'max': None}
y_range_points = {'min': None, 'max': None}
x_range_points1 = {'min': None, 'max': None}
y_range_points1 = {'min': None, 'max': None}

# Route cho trang chính
@app.route('/', methods=['GET', 'POST'])
def index():
    # Xử lý request POST từ form và render template tương ứng
    if request.method == 'POST':
        video_name = request.form['video_name']
        return render_template('play.html', video_name=video_name)
    # Nếu là request GET, render template 'index.html'
    return render_template('index.html')

# Route để lưu trữ các tọa độ được chọn
@app.route('/save_coordinates', methods=['POST'])
def save_coordinates():
    global clickedPoints, clickedPoints1, x_range_points, y_range_points, x_range_points1, y_range_points1
    # Nhận dữ liệu JSON từ frontend
    data = request.get_json()
    # Cập nhật danh sách các điểm được chọn và giá trị min/max của tọa độ X và Y
    clickedPoints = data.get('clickedPoints', [])
    clickedPoints1 = data.get('clickedPoints1', [])
    update_range_values(clickedPoints, x_range_points, y_range_points)
    update_range_values(clickedPoints1, x_range_points1, y_range_points1)
    return jsonify({'success': True})

# Route để xem các tọa độ đã được lưu trữ
@app.route('/view_coordinates', methods=['GET'])
def view_coordinates():
    global x_range_points, y_range_points, x_range_points1, y_range_points1
    # Trả về dữ liệu JSON chứa giá trị min/max của tọa độ X và Y cho cả hai loại điểm
    return jsonify({
        'x_range_points': x_range_points,
        'y_range_points': y_range_points,
        'x_range_points1': x_range_points1,
        'y_range_points1': y_range_points1
    })

# Hàm cập nhật giá trị min/max của tọa độ X và Y dựa trên danh sách các điểm được chọn
def update_range_values(points, x_range, y_range):
    x_values = [point['x'] for point in points]
    y_values = [point['y'] for point in points]

    x_range['min'] = min(x_values) if x_values else None
    x_range['max'] = max(x_values) if x_values else None
    y_range['min'] = min(y_values) if y_values else None
    y_range['max'] = max(y_values) if y_values else None

# Chạy ứng dụng và bật chế độ debug để theo dõi và sửa lỗi
if __name__ == '__main__':
    app.run(debug=True)
