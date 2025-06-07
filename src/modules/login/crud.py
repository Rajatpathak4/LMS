from fastapi import Depends, HTTPException
from modules.login.model import LoginUser
from modules.login import schema 
from modules.helper.GlobalFunction import printCustmessage, line_error_details
from datetime import datetime
import bcrypt 
from dependencies import create_access_token, get_current_user

def login(request, db):
    try:
        existing_user = db.query(LoginUser).filter(
            LoginUser.user_id == request.user_id,
            LoginUser.is_deleted == False 
        ).first()

        if existing_user:
            return printCustmessage(200, "FALSE", "Record already exists")

        hashed_password = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        new_user = LoginUser(
            user_id=request.user_id,
            password=hashed_password,
            created_at=datetime.utcnow(),
            is_deleted=False
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return printCustmessage(200, "TRUE", "User created successfully", {"user_id": new_user.user_id})

    except Exception as err:
        db.rollback()
        return line_error_details(err)

def authenticate_user(request, db):
    try:
        user = db.query(LoginUser).filter(
            LoginUser.user_id == request.user_id,
            LoginUser.is_deleted == False
        ).first()

        if not user:
            return printCustmessage(200, "FALSE", "User not found")

        if not bcrypt.checkpw(request.password.encode('utf-8'), user.password.encode('utf-8')):
            return printCustmessage(200, "FALSE", "Incorrect password")

        # Import your create_access_token from dependencies.py
        token = create_access_token({"id": user.id, "user_id": user.user_id})

        return printCustmessage(200, "TRUE", "Login successful", {"access_token": token, "token_type": "bearer"})

    except Exception as err:
        return line_error_details(err)
