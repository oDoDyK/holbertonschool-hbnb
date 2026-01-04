from app.models.BaseEntity import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def add_review(self, text):
        """Add a text to the review."""
        self.text.append(text)
