import requests
import vk
import vk_api

# делаем пост на главной страницу в вк

session = vk.AuthSession(app_id='7365787', user_login='***********',
                        user_password='**********', scope='wall, friends')
                        # user_login,user_password это ваши личные логин и пароль вк

api = vk.API(session, v='5.35')
api.wall.post(
    message='Oh, man... Are you Ok?',
)

print("Мой друг, с id=1 :")
user_with_id_one=api.users.get(user_ids=1)
print(user_with_id_one)

print("12 друзей Люции ")
friends_list=api.friends.get(fields='contacts',count=12)
print(friends_list)

#https://oauth.vk.com/blank.html#access_token=27ddec3dacf2f782e6a989d185aa8d2ff9e6b13b3701c34ee089127f42f989d70b8a92e12ea8efade401c&expires_in=0&user_id=185413339


