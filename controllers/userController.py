from models.User import User

def get_all_user():
    user = User.query.all();
    print(user)
    
    return [
        user.to_dict() 
        
        for user in User.query.all()]