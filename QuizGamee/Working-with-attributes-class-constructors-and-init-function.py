class User:
    pass # Just ignores...


user_1 = User

# How do we create an attribute for that class?
user_1.id = "001"
user_1.username = "Aditya"
# We can add as many attributes as we want into the class
# Now the user_1 object has attributes: username = "Aditya" and id = "001"

'''
However this is completely unique to the object (user_1) ... If we were to create 
another object from the class User, it will not have the attributes username and id
In other words if we want all objects using the same class have these 2 attributes,
we would have to define them repeatedly. This can be prone to error and confusion

Solution: Specify the starting pieces of  when I create my object from the class,
            so all objects will have the same beginning attributes
            This is also called initializing
            To do this we use a constructor or an __init__ function
            Here you initialize the attributes... 
'''


class UserTypeTwoInsta:
    def __init__(self, user_id, username):
        # Self is the actual object being initialized
        self.followers = 0 # 0 is defaulted
        self.id = user_id # the user_id to the right is the parameter
        self.username = username
        # In addition to self you can add as many parameters, which is going to be passed in when an object is created (parameters for the class)
        # Initialize attributes
        # Is called everytime a new object is created with this class
        # In other words a print statement will be triggered every time
        print("New user being created...")
        # Whenever a new object is created it must provide these 3 pieces of data (parameters)


my_user1 = UserTypeTwoInsta(user_id="001", username="aditya")
my_user2 = UserTypeTwoInsta(user_id="001", username="aditya")
# At the time of construction you can specify the attributes for the object
print(my_user1.followers) # Will be 0 since it was defaulted
print(my_user2.id)

'''
What about methods!!!!!!!!!!!!!!!!!!!!!!??????????? or Functions!!!!????
'''


class UserTypeThreeInsta:
    def __init__(self, user_id, username):
        self.followers = 0 # 0 is defaulted
        self.id = user_id # the user_id to the right is the parameter
        self.username = username
        self.following = 0 # Defaulted
        print("New user being created...")

    # Method: A way for users to follow each other
    def follow(self, user):
        # Methods in the class always needs a self parameter
        user.followers += 1
        self.following += 1


adi = UserTypeThreeInsta("004", "Adi")
achu = UserTypeThreeInsta("005", "Adi")
adi.follow(achu)
print(adi.following) # 1
print(achu.followers) # 1














