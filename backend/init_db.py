import database, models

def init_db():
    database.Base.metadata.create_all(bind=database.engine)
    db = database.SessionLocal()

    # Add sample exercises
    exercises = [
        models.Exercise(title="Columna Vertebral", description="Ejercicios de estiramiento y fortalecimiento para la espalda y cuello.", video_url="https://example.com/columna"),
        models.Exercise(title="Hombros", description="Rutinas para mejorar la movilidad y fuerza en la articulación del hombro.", video_url="https://example.com/hombros"),
        models.Exercise(title="Rodillas", description="Fortalecimiento de cuádriceps y ejercicios de impacto controlado.", video_url="https://example.com/rodillas"),
        models.Exercise(title="Caderas", description="Movimientos para mejorar la flexibilidad y estabilidad de la cadera.", video_url="https://example.com/caderas"),
        models.Exercise(title="Manos", description="Ejercicios de motricidad fina y estiramiento de tendones.", video_url="https://example.com/manos"),
        models.Exercise(title="Pies", description="Fortalecimiento de la planta del pie y ejercicios de equilibrio.", video_url="https://example.com/pies"),
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
