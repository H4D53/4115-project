from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory,Frontpage
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

    
class iphone(BaseView):
    default_view = 'iphone12_pro'
    
    @expose('/iphone12_pro/')
    def iphone12_pro(self):
        param1 = 'iphone12 pro'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)
    @expose('/iphone12/')
    def iphone12(self):
        param1 = 'iphone12'
        self.update_redirect()
        return self.render_template('news.html', param=param1)
    @expose('/iphone11/')
    def iphone11(self):
        param1 = 'iphone11'
        self.update_redirect()
        return self.render_template('news.html', param=param1)
    @expose('/iphoneSE/')
    def iphoneSE(self):
        param1 = 'iphoneSE'
        self.update_redirect()
        return self.render_template('news.html', param=param1)


class ipad(BaseView):
    default_view = 'iPad_Pro'

    @expose('/iPad_Pro/')
    def iPad_Pro(self):
        param1 = 'iPad Pro'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/iPad_Air/')
    def iPad_Air(self):
        param1 = 'iPad_Air'
        self.update_redirect()
        return self.render_template('news.html', param=param1)
    
    @expose('/iPad/')
    def iPad(self):
        param1 = 'iPad'
        self.update_redirect()
        return self.render_template('news.html', param=param1)
    @expose('/iPad_mini/')
    def iPad_mini(self):
        param1 = 'iPad_mini'
        self.update_redirect()
        return self.render_template('news.html', param=param1)


class Mac(BaseView):
    default_view = 'MacBook_Air'

    @expose('/MacBook_Air/')
    def MacBook_Air(self):
        param1 = 'MacBook_Air'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/MacBook_Pro_13/')
    def MacBook_Pro_13(self):
        param1 = 'MacBook_Pro_13'
        self.update_redirect()
        return self.render_template('news.html', param=param1)
    
    @expose('/MacBook_Pro_16/')
    def MacBook_Pro_16(self):
        param1 = 'MacBook_Pro_16'
        data = db.session.query(Frontpage).all()
        for da in data:
            print(da.heading)
        #log.error("Update ViewMenu error: {0}".format(str(data[0])))
        self.update_redirect()
        return self.render_template('news.html', datas=data)
        
   
db.create_all()

""" Page View """

appbuilder.add_view(Mac, 'MacBook Air', category="Mac")
appbuilder.add_link("MacBook Pro 13 inch", href="/mac/MacBook_Pro_13/", category="Mac")
appbuilder.add_link("MacBook Pro 16 inch", href="/mac/MacBook_Pro_16/", category="Mac")

appbuilder.add_view(iphone, "iphone12 Pro", category='iphone')
appbuilder.add_link("iphone12", href="/iphone/iphone12/", category="iphone")
appbuilder.add_link("iphone11", href="/iphone/iphone11/", category="iphone")
appbuilder.add_link("iphoneSE", href="/iphone/iphoneSE/", category="iphone")

appbuilder.add_view(ipad, 'iPad Pro', category="ipad")
appbuilder.add_link("iPad Air", href="/ipad/iPad_Air/", category="ipad")
appbuilder.add_link("iPad", href="/ipad/iPad/", category="ipad")
appbuilder.add_link("iPad mini", href="/ipad/iPad_mini/", category="ipad")
""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

appbuilder.add_view(FrontpageView, "Frontpage", icon="fa-folder-open-o", category="Admin")

