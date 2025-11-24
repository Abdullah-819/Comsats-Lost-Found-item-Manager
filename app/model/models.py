from app import db
import hashlib

# Password utilities

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed


# Base Item Class

class BaseItem(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    contact = db.Column(db.String(50))
    image_url = db.Column(db.String(200))
    status = db.Column(db.String(50), default='lost')

    def save(self):
        """Save item to database"""
        db.session.add(self)
        db.session.commit()

    def update_status(self, new_status):
        """Update item status"""
        self.status = new_status
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'contact': self.contact,
            'image_url': self.image_url,
            'status': self.status
        }
    
# Lost Item Class

class LostItem(BaseItem):
    __tablename__ = 'lost_items'
    submitted_by_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return f"<LostItem {self.name} at {self.location}>"

    def to_dict(self):
        data = super().to_dict()
        data['submitted_by_user'] = self.submitted_by_user
        return data

# Found Item Class

class FoundItem(BaseItem):
    __tablename__ = 'found_items'
    submitted_by_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return f"<FoundItem {self.name} at {self.location}>"

    def to_dict(self):
        data = super().to_dict()
        data['submitted_by_user'] = self.submitted_by_user
        return data
    
# User Class

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column('password', db.String(200), nullable=False)
    role = db.Column(db.String(50), default='user')  # user/admin

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, raw_password):
        self._password = hash_password(raw_password)

    def check_password(self, raw_password):
        return verify_password(raw_password, self._password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def promote_to_admin(self):
        self.role = 'admin'
        db.session.commit()

    def __repr__(self):
        return f"<User {self.name} ({self.role})>"
