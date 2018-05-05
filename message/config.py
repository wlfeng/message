import os

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    cookie_secret='FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI=',
    xsrf_cookies=True,
    debug=True
)

mysql_options = dict(
    host='www.wlfeng.cn',
    database='messageboard',
    user='wlfeng',
    password='Fwl54188'
)

log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
log_level = 'debug'

passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="
