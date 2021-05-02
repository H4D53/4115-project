import datetime
import random
import logging
import cgi
from .models import Gender, Country, Frontpage, iPad
from app import db

log = logging.getLogger(__name__)


def fill_gender():
    try:
        db.session.add(Gender(name='Male'))
        db.session.add(Gender(name='Female'))
        db.session.commit()
    except:
        db.session.rollback()


def fill_data():
    countries = ['Portugal', 'Germany', 'Spain', 'France', 'USA', 'China', 'Russia', 'Japan']
    for country in countries:
        c = Country(name=country)
        try:
            db.session.add(c)
            db.session.commit()
        except Exception as e:
            log.error("Update ViewMenu error: {0}".format(str(e)))
            db.session.rollback()

def fill_page():
    contents = [{"heading":'私隱',"sub_heading":'你的資料，由你話事',"point_1":'Safari 讓你避過追蹤',"point_2":'相片 App 保障你的影像，不會意外曝光。',"point_3":'訊息內容，只有接收者看得到',"point_4":'Siri 知你所需，卻不知道你是誰',"point_5":'銀包 App 和 Apple Pay，隨你購物，為你保密。',"point_6":'健康 App 保管你的資料記錄，密實穩妥。',"point_7":'地圖 App，你的定位記錄，定不記錄。',"background":"background:url('static/img/green_cup.png')","icon":"fa fa-bolt fa-5x"},
    {"heading":'AirTag',"sub_heading":'遺失東西的習慣，消失了',"point_1":'讓你超級輕鬆地追蹤你的物品。',"point_2":'呼叫它，找到它。',"point_3":'近，好近，非常近，搵到',"point_4":'多得千千萬萬人的一臂之力',"point_5":'何來神通廣大?',"point_6":'遺失模式，找尋更易找到',"point_7":'',"background":"background:url('static/img/fabric_1.png')","icon":"fa fa-list fa-5x"},
    {"heading":'WATCH', "sub_heading":'健康的未來，現在戴上',"point_1":'血氧感測 煥發創新氣息',"point_2":'突破性的感測器，了解更透徹',"point_3":'照亮深層，看個明明白白。',"point_4":'你的心，由指尖透露',"point_5":'',"point_6":'',"point_7":'',"background":"background:url('static/img/green_cup.png')","icon":"fa fa-cog fa-5x"},
    {"heading":'iPhone 12 Pro 及 iPhone 12 Pro Max',"sub_heading":'跨步，大飛躍',"point_1":'5G 一躍登上 Pro 系列',"point_2":'A14 仿生極速超前，遠遠拋離所有智能電話晶片',"point_3":'Pro 相機系統，將低光拍攝提升至嶄新層次，更在 iPhone 12 Pro Max 上登峰造極',"point_4":'陶瓷晶體護面，帶來四倍耐跌撞能力',"point_5":'實力非一般，來一起見識',"point_6":'細節，大有講究',"point_7":'',"background":"background:url('static/img/polaroid.png')","icon":"fa fa-lock fa-5x"}]
    for content in contents:
        try:
            db.session.add(Frontpage(heading=content["heading"],sub_heading=content["sub_heading"],point_1=content["point_1"],point_2=content["point_2"],point_3=content["point_3"],point_4=content["point_4"],point_5=content["point_5"],point_6=content["point_6"],point_7=content["point_7"],background=content["background"],icon=content["icon"]))
            db.session.commit()
        except Exception as e:
            log.error("Update ViewMenu error: {0}".format(str(e)))
            db.session.rollback()

