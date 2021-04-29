from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


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
        self.update_redirect()
        return self.render_template('news.html', param=param1)


db.create_all()

""" Page View """
appbuilder.add_view(iphone, "iphone12 Pro", category='iphone')
appbuilder.add_link("iphone12", href="/iphone/iphone12/", category="iphone")
appbuilder.add_link("iphone11", href="/iphone/iphone11/", category="iphone")
appbuilder.add_link("iphoneSE", href="/iphone/iphoneSE/", category="iphone")

appbuilder.add_view(Mac, 'MacBook Air', category="Mac")
appbuilder.add_link("MacBook Pro 13 inch", href="/Mac/MacBook_Pro_13/", category="Mac")
appbuilder.add_link("MacBook Pro 16 inch", href="/Mac/local_news/", category="Mac")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

