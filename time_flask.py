from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_current_time():
    # You can change the timezone as needed
    timezone = pytz.timezone('Asia/Shanghai')
    now = datetime.now(timezone)
    return now.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)
