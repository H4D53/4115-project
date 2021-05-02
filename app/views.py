from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory,Frontpage,iPad,iPhone,Mac,Watch
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView
import json
import logging
log = logging.getLogger(__name__)

def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class FrontpageView(ModelView):
    datamodel = SQLAInterface(Frontpage)
    list_columns = ['id','heading','sub_heading','point_1','point_2','point_3','point_4','point_5','point_5','point_6','point_7','background','icon']

class iPadView(ModelView):
    datamodel = SQLAInterface(iPad)
    list_columns = ['img','id','models','iPadsize','chip','wifi','USB_type']

class WatchView(ModelView):
    datamodel = SQLAInterface(Watch)
    list_columns = ['img','models','watchsize','gps','function','internet']

class MacView(BaseView):
    datamodel = SQLAInterface(Mac)
    list_columns = ['img','models','DisplaySize','chip','wifi','bluetooth']
    
class iPhoneView(ModelView):
    datamodel = SQLAInterface(iPhone)
    list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
    
class iphone(BaseView):
    default_view = 'iphone12_pro'
    
    @expose('/iphone12_pro/')
    def iphone12_pro(self):
        param1 = 'iphone12 pro'
        self.update_redirect()
        datas = db.session.query(iPhone).filter_by(models='iPhone 12 Pro').all()
        list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)
    @expose('/iphone12/')
    def iphone12(self):
        param1 = 'iphone12'
        self.update_redirect()
        datas = db.session.query(iPhone).filter_by(models='iPhone 12').all()
        list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)
    @expose('/iphone11/')
    def iphone11(self):
        param1 = 'iphone11'
        self.update_redirect()
        datas = db.session.query(iPhone).filter_by(models='iPhone 11').all()
        list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)
    @expose('/iphoneSE/')
    def iphoneSE(self):
        param1 = 'iphoneSE'
        self.update_redirect()
        datas = db.session.query(iPhone).filter_by(models='iPhone SE').all()
        list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)


class watch(BaseView):
    default_view = 'Watch6'
    
    @expose('/Watch6/')
    def Watch6(self):
        param1 = 'Watch6 pro'
        self.update_redirect()
        datas = db.session.query(Watch).filter_by(models='Apple Watch Series 6').all()
        list_columns = ['img','models','watchsize','gps','function','internet']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)
    @expose('/WatchSE/')
    def WatchSE(self):
        param1 = 'WatchSE'
        self.update_redirect()
        datas = db.session.query(Watch).filter_by(models='Apple Watch SE').all()
        list_columns = ['img','models','watchsize','gps','function','internet']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)
    @expose('/Watch3/')
    def Watch3(self):
        param1 = 'Watch3'
        self.update_redirect()
        datas = db.session.query(Watch).filter_by(models='Apple Watch Series 3').all()
        list_columns = ['img','models','watchsize','gps','function','internet']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)



class ipad(BaseView):
    default_view = 'iPadPro'

    @expose('/iPadPro/')
    def iPadPro(self):
        param1 = 'iPadPro'
        self.update_redirect()
        datas = db.session.query(iPad).filter_by(models='iPad Pro').all()
        list_columns = ['img','models','iPadsize','chip','wifi','USB_type']
        return self.render_template('ipad.html', datas=datas,list_columns=list_columns)
    
    @expose('/iPadAir/')
    def iPadAir(self):
        param1 = 'iPadAir'
        self.update_redirect()
        datas = db.session.query(iPad).filter_by(models='iPad Air').all()
        list_columns = ['img','models','iPadsize','chip','wifi','USB_type']
        return self.render_template('ipad.html', datas=datas,list_columns=list_columns)
    @expose('/iPad/')
    def iPad(self):
        param1 = 'iPad'
        self.update_redirect()
        datas = db.session.query(iPad).filter_by(models='iPad').all()
        list_columns = ['img','models','iPadsize','chip','wifi','USB_type']
        return self.render_template('ipad.html', datas=datas,list_columns=list_columns)
    @expose('/iPadmini/')
    def iPadmini(self):
        param1 = 'iPadmini'
        self.update_redirect()
        datas = db.session.query(iPad).filter_by(models='iPad mini').all()
        list_columns = ['img','models','iPadsize','chip','wifi','USB_type']
        return self.render_template('ipad.html', datas=datas,list_columns=list_columns)
    




        

class mac(BaseView):
    default_view = 'MacBook_Air'

    @expose('/MacBook_Air/')
    def MacBook_Air(self):
        param1 = 'MacBook_Air'
        self.update_redirect()
        datas = db.session.query(iPhone).filter_by(id=101).all()
        list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)

    @expose('/MacBook_Pro_13/')
    def MacBook_Pro_13(self):
        param1 = 'MacBook_Pro_13'
        self.update_redirect()
        datas = db.session.query(iPhone).filter_by(id=102).all()
        list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)
    
    @expose('/MacBook_Pro_16/')
    def MacBook_Pro_16(self):
        param1 = 'MacBook_Pro_16'
        self.update_redirect()
        datas = db.session.query(iPhone).filter_by(id=103).all()
        list_columns = ['img','models','iPhonesize','chip','wifi','USB_type']
        return self.render_template('iphone.html', datas=datas,list_columns=list_columns)

db.create_all()

""" Page View """

# appbuilder.add_view(Register, 'Register', category="Sam")

appbuilder.add_view(mac, 'MacBook Air', category="Mac")
appbuilder.add_link("MacBook Pro 13 inch", href="/mac/MacBook_Pro_13/", category="Mac")
appbuilder.add_link("MacBook Pro 16 inch", href="/mac/MacBook_Pro_16/", category="Mac")

appbuilder.add_view(iphone, "iphone12 Pro", category='iPhone')
appbuilder.add_link("iphone12", href="/iphone/iphone12/", category="iPhone")
appbuilder.add_link("iphone11", href="/iphone/iphone11/", category="iPhone")
appbuilder.add_link("iphoneSE", href="/iphone/iphoneSE/", category="iPhone")

appbuilder.add_view(ipad, 'iPad Pro', category="iPad")
appbuilder.add_link("iPad Air", href="/ipad/iPadAir/", category="iPad")
appbuilder.add_link("iPad", href="/ipad/iPad/", category="iPad")
appbuilder.add_link("iPadmini", href="/ipad/iPadmini/", category="iPad")

appbuilder.add_view(watch, 'Apple Watch Series 6', category="watch")
appbuilder.add_link("Apple Watch SE", href="/watch/WatchSE/", category="watch")
appbuilder.add_link("Apple Watch Series 3", href="/watch/Watch3/", category="watch")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(FrontpageView, "Frontpage", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(iPadView, "iPad", icon="fa-folder-open-o", category="Admin")
#appbuilder.add_view(MacView, "Mac", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(WatchView, "Watch", icon="fa-folder-open-o", category="Admin")