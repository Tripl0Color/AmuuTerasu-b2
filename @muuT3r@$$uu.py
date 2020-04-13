import vk_requests
import time
id = 123                           # Вставь сюда свой айди ( id = 472165736 )
pst =  123                         # Вставь сюда айди поста ( pst = 1 )
#pst2 = 123                        # Если нужно 2 поста, убери решетку после 12 строки,и здесь
t = 5                              # Время перед постами

print ("""
Working.
@muuT3ra$$uu b2
#FuckAll.Everything. 
by Tripl_color vk.com/Tripl_color""")

msg = "@muuT3ra$$uu b2 , #FuckAll.Everything. by Tripl_color vk.com/Tripl_color" # Сообщение в коментариях
while True:
 api = vk_requests.create_api(service_token="Paste token here")                          # Введи сюда токен группы от которой можно оставлять коментарии
 print(api.wall.createComment(owner_id= id, post_id= pst, message= msg))
 time.sleep(t)
 #api = vk_requests.create_api(service_token="Paste token here")
 #print(api.wall.createComment(owner_id= id, post_id= pst2, message= msg))
 #time.sleep(t)
