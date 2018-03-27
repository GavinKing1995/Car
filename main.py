# coding=utf-8
"""
日期：2018.3.26
版本：v1.2
功能：微信群约车脚本，自动回复约车信息
更新：修复print乱码问题
"""

import itchat
import sys
import time
from itchat.content import *

reload(sys)
sys.setdefaultencoding('utf8')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    transmit = ""
    if msg['ActualNickName'] == "康教练" and \
            ("上午科二" in msg['Content'] or "下午科二" in msg['Content'] or \
             "科二全天" in msg['Content'] or "全天科二" in msg['Content']):
        if "上午科二" in msg['Content']:
            transmit = "上午两人"
        if "下午科二" in msg['Content']:
            transmit = "下午两人"
        if "科二全天" in msg['Content'] or "全天科二" in msg['Content']:
            transmit = "全天两人"
        msg.user.send("%s" % transmit)
        print("%s\tLog:发送者为:%s" % (time.ctime(), msg['ActualNickName']))
        print("%s\tLog:接收内容为:%s\n%s\tLog:回复内容为:%s\n" % (time.ctime(), msg['Content'], time.ctime(), transmit))
        # print("%s\tLog:回复内容为:%s\n" % (time.ctime(), transmit))


itchat.auto_login(hotReload=True, enableCmdQR=True)
itchat.run()
