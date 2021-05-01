from flask_appbuilder.views import IndexView
from flask_appbuilder.views import expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Frontpage

class FABView(IndexView):
    """
        A simple view that implements the index for the site
    """
    index_template = 'index.html'
    datamodel = SQLAInterface(Frontpage)
    list_columns = ['background','icon','heading','sub_heading','point_1','point_2','point_3','point_4','point_5', 'point_6','point_7']
    
    @expose('/')
    def index(self):
        self.update_redirect()
        datas = self.datamodel.session.query(Frontpage).all()
        return self.render_template(self.index_template, datas=datas, appbuilder=self.appbuilder, list_columns=self.list_columns)
 
   