import database, models

def init_db():
    database.Base.metadata.create_all(bind=database.engine)
    db = database.SessionLocal()

    # Add sample exercises
    exercises = [
        models.Exercise(title="Lumbar Stretch", description="Basic stretch for lower back pain.", video_url="https://example.com/lumbar"),
        models.Exercise(title="Neck Mobilization", description="Gentle movements to reduce neck stiffness.", video_url="https://example.com/neck"),
    ]

    # Add sample treatments
    treatments = [
        models.Treatment(name="Manual Therapy", description="Hands-on techniques for joint and muscle mobilization."),
        models.Treatment(name="Electrotherapy", description="Use of electrical energy for healing."),
    ]

    db.add_all(exercises)
    db.add_all(treatments)
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
