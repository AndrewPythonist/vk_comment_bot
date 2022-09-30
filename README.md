# vk_comment_bot

**Что делает бот?**

vk_comment_bot нужен для авто-комментирования постов других пабликов от имени вашей группы.
Бот берет рандомные сообщения и картинки из подготовленной базы, постоянно детектит выпуск новых постов в группах(из подготовленного списка групп) и как можно раньше оставляет комментарии от имени группы.

Вот как примерно это выглядит
![](https://github.com/AndrewPythonist/vk_spam_bot/raw/master/comment-example.png)

Сама работа бота основанна на баге(который вконтакте так и не исправили за 3 года🙃). Суть в том что с фейковой страницы мы берем токен для группы, аккаунт банят, но токен и следовательно бот остается рабочим.

**Как настроить бота и начать им пользоваться?**

Для начала нам нужно подготовить все материалы для бота, все это заполняется в файле data.py

*token*
для работы бота нам необходимо получить токен с фейковой страницы(т.к. ее потом заблокируют), дайте права администратора фейковой странице и затем получите токен:
Управление --> Настройки --> Работа с API --> Создать ключ --> отметить галочку "Разрешить приложению доступ к управлению сообществом" --> а затем подтвердите получение токена по смс или уведомлению --> скопируйте его и вставьте в переменную *token*

***mygroup_id***  
id вашего паблика вставить в переменную *mygroup_id*

***groups*** 
Подготовьте id адреса всех групп куда бот будет рассылать комментарии. Вставьте их в список *groups* через запятую, каждый id должен начинаться со знака минус. 

***messages*** 
Вставьте сообщения для комментирования в список *messages*

***pictures*** 
Заранее загрузите все фото для комментариев бота в отдельный альбом вконтакте(желательно на другой фейковой странице). Затем вставьте эти адреса в список *pictures* в формате 'photo<id страницы>_<id фотографии>'


Запуск бота:
python3 v6.py
