# import random
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
#
# def measure_threat_level(ip_address):
#     if ip_address == '1':
#         return 'Low'
#     elif ip_address == '2':
#         return 'Medium'
#     elif ip_address == '3':
#         return 'High'
#     else:
#         return 'Unknown'
#
#
# def generate_logs(ip_address):
#     logs = []
#     for i in range(5):
#         logs.append(f"Log {i + 1} for {ip_address}")
#     return logs
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         ip_address = request.form['ip_address']
#         threat_level = measure_threat_level(ip_address)
#         logs = generate_logs(ip_address)
#         return render_template('index.html', ip_address=ip_address, threat_level=threat_level, logs=logs)
#     else:
#         return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# version 2

from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)


# Generate random mock data for thermometer values
def generate_mock_data():
    return {
        'category1': random.randint(0, 100),
        'category2': random.randint(0, 100),
        'category3': random.randint(0, 100)
    }


@app.route('/')
def index():
    return render_template('thermometer.html')


@app.route('/mock-data')
def get_mock_data():
    return jsonify(generate_mock_data())


if __name__ == '__main__':
    app.run()
