from pathlib import Path
from nonebot.plugin import PluginMetadata
from .config import Config
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command
import random


# 发布插件配置，暂未配置好，先别看
__plugin_meta__ = PluginMetadata(
    name="cecilia",
    description="一个向群内发送白圣女cecilia的插件",
    usage="{插件用法}",


    type="{插件分类}",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。


    homepage="{项目主页}",
    # 发布必填。


    config=Config,
    # 插件配置项类，如无需配置可不填写。


    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)

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
    num = random.randint(1,40)
    image = MessageSegment.image(local + str(num) + ".png")
    # 发送图片
    await network_picture.finish(image)
