from app import create_app
from app.model.models import db, User, LostItem, FoundItem

# -----------------------------
# Setup Flask app context
# -----------------------------
app = create_app()
with app.app_context():
    
    # -----------------------------
    # Reset database (for testing)
    # -----------------------------
    db.drop_all()
    db.create_all()

    # -----------------------------
    # Test User creation
    # -----------------------------
    user = User(name="Test User", email="testuser@example.com")
    user.password = "password123"  # Encapsulation in action
    user.save()
    print("User created:", user)

    # -----------------------------
    # Test LostItem creation
    # -----------------------------
    lost_item = LostItem(
        name="Test Lost Item",
        description="Lost in Library",
        location="Library",
        contact="0321-000111",
        image_url="static/images/image1.jpeg",
        submitted_by_user=user.id
    )
    lost_item.save()
    print("Lost Item created:", lost_item)

    # -----------------------------
    # Test FoundItem creation
    # -----------------------------
    found_item = FoundItem(
        name="Test Found Item",
        description="Found in Cafeteria",
        location="Cafeteria",
        contact="0321-000222",
        image_url="static/images/image2.jpeg",
        status="found",
        submitted_by_user=user.id
    )
    found_item.save()
    print("Found Item created:", found_item)

    # -----------------------------
    # Test updating status
    # -----------------------------
    lost_item.update_status("resolved")
    print("Updated Lost Item status:", lost_item.status)

    # -----------------------------
    # Test User role promotion
    # -----------------------------
    user.promote_to_admin()
    print("Promoted User role:", user.role)

    # -----------------------------
    # Test to_dict() method
    # -----------------------------
    print("Lost item as dict:", lost_item.to_dict())
    print("Found item as dict:", found_item.to_dict())
