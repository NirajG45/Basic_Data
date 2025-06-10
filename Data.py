from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "labels": ["Python", "C++", "C", "MongoDB", "SQL", "MySQL"],
        "values": [92, 85, 78, 80, 88, 90]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
