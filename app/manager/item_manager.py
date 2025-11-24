from app.model.models import LostItem, FoundItem

def get_lost_items():
    return LostItem.query.all()

def get_found_items():
    return FoundItem.query.all()
