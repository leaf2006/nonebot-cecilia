from pathlib import Path

from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command
import random

# 本地发送信息，一般情况下不会用这个

# local_picture = on_command("白圣女")

# @local_picture.handle()
# async def handle_local_picture():
#     # 本地图片位置
#     path = Path(__file__).parent / "cecilia"".png"
#     # 构造图片消息段
#     image = MessageSegment.image(path)
#     # 发送图片
#     await local_picture.finish(image)

network_picture = on_command("白圣女",aliases={"我要看白圣女","cecilia"})

@network_picture.handle()
async def handle_network_picture():
    
    # 构造图片消息段
    url = "https://cdn.jsdelivr.net/gh/leaf2006/cecilia-img/" #使用github并使用jsdelivr进行cdn加速，但是速度依然不佳，有可能会timeout，但也不是不能用
    local = "http://172.24.28.97:1234/" #本地服务器，如果github端出现timeout的情况，可以在本地部署，速度更快
    # direct = "https://raw.githubusercontent.com/leaf2006/cecilia-img/main/"
    num = random.randint(1,21)
    image = MessageSegment.image(local + str(num) + ".png")
    # 发送图片
    await network_picture.finish(image)
