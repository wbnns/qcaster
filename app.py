from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queue.db'
db = SQLAlchemy(app)

class Queue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        new_item = Queue(text=text)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    items = Queue.query.all()
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)

