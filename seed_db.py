from app import create_app, db
from models import Category

app = create_app()

with app.app_context():
    # Create tables if they don't exist (this will create Category and others in MySQL)
    db.create_all()
    
    # Seed Categories
    categories = ['Academic', 'Sports', 'Culture', 'Workshop', 'Seminar', 'Hostel']
    for category_name in categories:
        if not Category.query.filter_by(name=category_name).first():
            db.session.add(Category(name=category_name))
            print(f"Added category: {category_name}")
    
    db.session.commit()
    print("Database seeded successfully.")
