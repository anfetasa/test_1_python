from app.services import user_service

def get_user_data():
    return user_service.get_fixed_user_data()
