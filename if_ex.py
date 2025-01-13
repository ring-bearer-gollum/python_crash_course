banned_users=['david','simon','sauron']
user_name='david'
if user_name not in banned_users:
    print('Hello '+user_name.title()+' you can post comment. If yu wish')
else:
    print(user_name.title()+' you have been banned..!')