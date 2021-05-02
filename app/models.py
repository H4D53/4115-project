import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class Frontpage(Model):
     __tablename__ = 'frontpage'
     id = Column(Integer, primary_key=True)
     heading = Column(String(50), nullable=False)
     sub_heading = Column(String(50), nullable=False)
     point_1 = Column(String(50), nullable=True)
     point_2 = Column(String(50), nullable=True)
     point_3 = Column(String(50), nullable=True)
     point_4 = Column(String(50), nullable=True)
     point_5 = Column(String(50), nullable=True)
     point_6 = Column(String(50), nullable=True)
     point_7 = Column(String(50), nullable=True)
     background = Column(String(50), nullable=True)
     icon = Column(String(50), nullable=True)
     

class iPad(Model):
     __tablename__ = 'iPad'
     id = Column(Integer, primary_key=True)
     img = Column(String(50), nullable=False)
     models = Column(String(50), nullable=False)
     iPadsize = Column(String(50), nullable=False)
     chip = Column(String(50), nullable=False)
     wifi = Column(String(50), nullable=True)
     USB_type = Column(String(50), nullable=True)
     

class Watch(Model):
     __tablename__ = 'Watch'
     id = Column(Integer, primary_key=True)
     img = Column(String(50), nullable=False)
     models = Column(String(50), nullable=False)
     watchsize = Column(String(50), nullable=False)
     gps = Column(String(50), nullable=False)
     function = Column(String(50), nullable=True)
     internet = Column(String(50), nullable=True)
    
class Mac(Model):
    __tablename__ = 'Mac'
    id = Column(Integer, primary_key=True)
    img = Column(String(50), nullable=False)
    models = Column(String(50), nullable=False)
    DisplaySize = Column(String(50), nullable=False)
    chip = Column(String(50), nullable=False)
    wifi = Column(String(50), nullable=True)
    bluetooth = Column(String(50), nullable=True)

class MacCategory(Model):
    __tablename__ = 'mac_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class iPhone(Model):
    __tablename__ = 'iPhone'
    id = Column(Integer, primary_key=True)
    img = Column(String(50), nullable=False)
    models = Column(String(50), nullable=False)
    iPhonesize = Column(String(50), nullable=False)
    chip = Column(String(50), nullable=False)
    wifi = Column(String(50), nullable=True)
    USB_type = Column(String(50), nullable=True)


class iPhoneCategory(Model):
    __tablename__ = 'iphone_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)