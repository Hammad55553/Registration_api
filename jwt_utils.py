# #jwt_utils.py

# import jwt
# from datetime import datetime, timedelta
# from passlib.context import CryptContext
# from dotenv import load_dotenv
# import os
# from fastapi import HTTPException, status

# load_dotenv()  # Load environment variables from a .env file

# SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")  # Secret key should be loaded from an env file in production
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Set token expiration time

# # Set up password hashing using passlib
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Function to hash a password
# def hash_password(password: str):
#     return pwd_context.hash(password)

# # Function to verify the password
# def verify_password(plain_password: str, hashed_password: str):
#     return pwd_context.verify(plain_password, hashed_password)

# # Function to create an access token
# def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# # Function to decode the token
# def decode_access_token(token: str):
#     try:
#         # Decoding the token and checking its validity
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Token has expired"
#         )
#     except jwt.PyJWTError as e:
#         # For any other JWT errors
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token"
#         )
