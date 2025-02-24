from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 메모 모델
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "content": self.content}