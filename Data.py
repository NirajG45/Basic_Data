from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "labels": ["Python", "C++", "C", "MongoDB", "SQL", "MySQL"],
        "values": [92, 85, 78, 80, 88, 90],
        "colors": [
            "#3572A5",  # Python - Blue
            "#f34b7d",  # C++ - Pink
            "#555555",  # C - Dark Gray
            "#13AA52",  # MongoDB - Green
            "#336791",  # SQL - Blue-Grey
            "#00758F"   # MySQL - Teal Blue
        ]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
