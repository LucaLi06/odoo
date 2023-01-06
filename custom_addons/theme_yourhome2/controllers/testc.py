from odoo import http
from odoo.http import request


class Hospital(http.Controller):

   @http.route('/patient_test/', type="http",auth="public",website="true")
   def patient_webform(self,**kw):
        return http.request.render('theme_yourhome2.create_test',{})

   @http.route('/create/test/', type="http", auth="public", website="true")
   def create_webpatient(self, **kw):
       print("oui")
       print("----",kw)
       request.env('yh.test').sudo().create(kw)
       return request.render("theme_yourhome2.create_test", {})
