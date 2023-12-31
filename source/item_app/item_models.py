from source.extensions import db

item_user = db.Table(

    'item_user',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
)


class Item(db.Model):
    # __tablename__ = 'Item'
    # query: db.Query = db.session.query_property()
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    image = db.Column(db.String(140))
    favorited_users = db.relationship('User', secondary=item_user, backref=db.backref('favorited_items', lazy='dynamic'), lazy='dynamic')

# class Inquiry(db.Model):
#     id
#     email
#     phone_number
#     name
#     description
