# from fastapi import APIRouter, HTTPException
# from app.models import UserRegistration
# from app.database import add_user_to_db, get_user
# from passlib.context import CryptContext
# from app.email_utils import send_registration_email
# from datetime import timedelta, datetime
# from jose import JWTError, jwt

# # Router setup
# auth_router = APIRouter()

# # Password hashing setup
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # JWT Configuration
# SECRET_KEY = "your_secret_key_here"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # Hash the password
# def hash_password(password: str):
#     return pwd_context.hash(password)

# # Generate the JWT token
# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta if expires_delta else datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # Registration endpoint
# @auth_router.post("/register", tags=["Authentication"])
# async def register_user(user: UserRegistration):
#     # Check if the username already exists
#     existing_user = await get_user(user.username)
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already exists")
    
#     # Hash the password before saving
#     hashed_password = hash_password(user.password)
    
#     # Save the user to the database
#     await add_user_to_db(user.username, user.email, hashed_password)

#     # Generate the access token for the user
#     access_token = create_access_token(
#         data={"sub": user.username},
#         expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     )

#     # Send the registration email
#     send_registration_email(user.email)

#     # Return the response with the token
#     return {"message": "User registered successfully", "access_token": access_token, "token_type": "bearer"}
