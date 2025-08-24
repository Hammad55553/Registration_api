from sqlalchemy.orm import Session
from . import models, schemas

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name, email=user.email, password=user.password, date_of_birth=user.date_of_birth
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
