from .. import db


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    weight = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    # the many-to-one relation
    size_id = db.Column(db.Integer, db.ForeignKey('pizza_sizes.id'))
    size = db.relationship("Size")

    def __repr__(self):
        return '<Пицца {} {} см ({} гр)>'.format(
            self.title, self.size, self.weight)


class Size(db.Model):
    __tablename__ = 'pizza_sizes'

    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)
    size_value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return str(self.size_value)
