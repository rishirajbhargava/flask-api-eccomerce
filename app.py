from flask import Flask , jsonify  , request  , render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    created_at = db.Column(db.DateTime , default=datetime.utcnow)

    def to_dict(self):
        return dict(id=self.id, name=self.name, email=self.email, created_at=self.created_at)
    

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_name = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime , default=datetime.utcnow)

    def to_dict(self):
        return dict(id=self.id, user_id=self.user_id, product_name=self.product_name, quantity=self.quantity, total_price=self.total_price, created_at=self.created_at)
    



with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        user = User(name=request.form['name'], email=request.form['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict())

    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    return jsonify(user.to_dict())

@app.route('/orders' , methods=['GET' , 'POST'])
def orders():
    if request.method == 'POST':
        order = Order(user_id=request.form['user_id'], product_name=request.form['product_name'], quantity=request.form['quantity'], total_price=request.form['total_price'])
        db.session.add(order)
        db.session.commit()
        return jsonify(order.to_dict())
    
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@app.route('/orders/<int:id>')
def get_order(id):
    order = Order.query.get(id)
    return jsonify(order.to_dict())

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
