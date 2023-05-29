from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///company.db'
db = SQLAlchemy(app)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    term = db.Column(db.Integer, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        term = request.form['term']
        company = Company(name=name, term=term)
        db.session.add(company)
        db.session.commit()

    companies = Company.query.all()
    total_service = sum([company.term for company in companies])
    return render_template('index.html', companies=companies, total_service=total_service)


if __name__ == '__main__':
    app.run(debug=True)