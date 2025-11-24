from app import create_app, db
from app.model.models import LostItem

app = create_app()

with app.app_context():
    
    # Delete all LostItem records

    num_deleted = LostItem.query.delete()
    db.session.commit()
    print(f"Deleted {num_deleted} lost items from the database.")
