## Небольшой проектик для сбора статистики по тратам на авто

При этом он в основном для прокачки
 - vue, vuex
 - python, mysql, fastApi
 - docker 
 которые подтянуть бы не мешало.

 # TODO:
 - в token.py залит jwt token, который надо нормально сохранять(или не надо?)
 - токен генерится без его обновления(навечно походу). Надо вернуть время его жизни. + выяснить как обновление будет срабатывать если еще на сайте
 
### список ошибок на порешать
...

 
### bug
херня какая-то с blueimp-md5 - в package.json хреново прописан
Заработал только через

    docker exec -it accounting_analitic_frontend_1 sh
    в нем тупо 'npm install blueimp-md5' и все норм. wtf?

 
