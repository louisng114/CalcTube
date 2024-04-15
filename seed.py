from models import Topic, db
from app import app

with app.app_context():
    db.create_all()

topics = [
    Topic(
        name="Overview",
        description="The idea of calculus in a broad stoke"
        ),
    Topic(
        name="Limits and Continuity",
        description="""How limits help us to handle change at an instant; \n
            Definition and properties of limits in various representations; \n
            Definitions of continuity of a function at a point and over a domain; \n
            Asymptotes and limits at infinity; \n
            Reasoning using the Squeeze theorem and the Intermediate Value Theorem
            """
        ),
    Topic(
        name="Exam Information",
        description="Information about the AP exam"
        ),
]

with app.app_context():
    db.session.add_all(topics)
    db.session.commit()