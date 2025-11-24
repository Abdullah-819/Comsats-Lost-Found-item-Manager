from app import create_app, db
from app.model.models import User, LostItem, FoundItem

app = create_app()

with app.app_context():  # Ensure app context is active
    db.create_all()  # Create tables

    # Create User
    user = User(name="Test User", email="testuser@example.com")
    user.password = "password123"
    user.save()
    print("User created:", user)

    # Create LostItem
    lost_item = LostItem(
        name="Test Lost Item",
        description="Lost in Library",
        location="Library",
        contact="0321-000111",
        image_url="static/images/image1.jpeg"
    )
    lost_item.save()
    print("Lost Item created:", lost_item)

    # Create FoundItem
    found_item = FoundItem(
        name="Test Found Item",
        description="Found in Cafeteria",
        location="Cafeteria",
        contact="0321-000222",
        image_url="static/images/image2.jpeg",
        status="found"
    )
    found_item.save()
    print("Found Item created:", found_item)

    # Update status
    lost_item.update_status("resolved")
    print("Updated Lost Item status:", lost_item.status)

    # Promote User
    user.promote_to_admin()
    print("Promoted User role:", user.role)

    # to_dict
    print("Lost item as dict:", lost_item.to_dict())
