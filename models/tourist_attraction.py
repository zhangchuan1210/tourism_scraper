# models/tourist_attraction.py

from extensions import db

class TouristAttraction(db.Model):
    __tablename__ = 'tourist_attractions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    user_name = db.Column(db.String(200), nullable=False)
    travel_link = db.Column(db.String(200), nullable=True)
    user_auth = db.Column(db.String(200), nullable=True)
    user_tag = db.Column(db.String(200), nullable=True)
    date = db.Column(db.String(200), nullable=True)
    days = db.Column(db.Integer, nullable=True)
    trip = db.Column(db.Text, nullable=True)
    route = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<TouristAttraction {self.title}>"
