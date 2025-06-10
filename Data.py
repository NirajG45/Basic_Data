from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data for visualization
    data = {
        "labels": ["Math", "Science", "English", "History", "Art"],
        "values": [88, 75, 90, 70, 95]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
