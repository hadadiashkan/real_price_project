from datetime import datetime

from real_price.extensions import db


class PriceHistory(db.Model):
    """price history model"""

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    ratio = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PriceHistory {self.name}>"
