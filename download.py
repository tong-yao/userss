# -*- coding: utf-8 -*-

import upyun, random, uuid, hashlib, pymysql, time
import hashlib, requests, re, logging
from datetime import datetime, timedelta
from faker import Faker

logging.basicConfig(filename="/var/www/namephoto/userssss/log.txt", filemode="a",
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.INFO)

# 需要填写自己的服务名，操作员名，密码
service = "qukanba-test"
username = "zhaoyining"
password = "QrNy0WvD9BTfPW3lWIes14vOg4Sg7N12"

# 需要填写上传文件的本地路径和云存储路径，目录
local_file = ""
remote_file = ""
remote_dir = "users_photos"

up = upyun.UpYun(service, username=username, password=password)

conn = pymysql.connect(host="39.97.241.144", port=3306, user="lianzhuoxinxi", passwd="LIANzhuoxinxi888?", db="spider",
                       charset="utf8mb4")
lis = []
row = 2000
page = 1


def getName():
    if len(lis) < 5:
        try:
            with conn.cursor() as cursor:
                global page
                sql = "select name from fake_user_copy1 limit {}, {}".format(int((page - 1) * row), row)
                cursor.execute(sql)
                cc = cursor.fetchall()
                page = page + 1
                for b, in cc:
                    lis.insert(0, b)
        except Exception as e:
            print(e)
    return lis.pop()


li = []
rows = 2000
beisiliushisi = ''

num = 0


def ava():
    if len(li) < 5:
        try:
            global beisiliushisi
            global num
            res = up.get_list_with_iter('%s' % remote_dir, limit=rows, begin="%s" % beisiliushisi)
            num += 1
            beisiliushisi = res["iter"]
            logging.INFO("第{}次进来".format(num))
            logging.INFO("base64是{}".format(beisiliushisi))

            print(beisiliushisi)

            for i in res['files']:
                li.insert(0, i["name"])
        except Exception as e:
            print(e)
    return li.pop(0)


fake = Faker()
a = fake.date(pattern="%Y-%m-%d", end_datetime=None)
for i in range(105000):
    avatars = ava()
    avatar = "/users_photos/" + avatars
    print(avatar)

    # births = a.replace("-", "")
    # birth = int(births)
    # print(birth)
    #
    # genders = random.randint(0, 1)
    # gender = str(genders)

    nickname = re.sub('[/\n]', '', getName())
    print("nickname", nickname)

    # rands = uuid.uuid4()
    # rand = str(rands)
    #
    # secret = "e6f9fdda5fa04a3f3a43f28b7c1c6cdd"
    #
    # miyao = "avatar=" + avatar + "&" + "birth=" + births + "&" + "gender=" + gender + "&" + "nickname=" + nickname + "&" + "rand=" + rand + secret
    # print(miyao)
    # md5 = hashlib.md5()
    # md5.update(str(miyao).encode())
    # namename = md5.hexdigest()
    #
    # response = requests.post("https://api.qkb-test.admin.lianzhuoxinxi.com/web/user/add",
    #                          data={"avatar": avatar, "birth": birth, "gender": genders, "nickname": nickname,
    #                                "rand": rand, "sign": namename})
    #
    # print(response.content.decode())
