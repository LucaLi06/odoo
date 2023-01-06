from odoo import http
from odoo.http import request


class Hospital(http.Controller):

   @http.route('/patient_webform2/', type="http",auth="public",website="true")
   def patient_webform(self,**kw):
        return http.request.render('theme_yourhome2.create_patient2',{})

   @http.route('/create/webpatient2/', type="http", auth="public", website="true")
   def create_webpatient(self, **kw):
       print("oui")
       request.env('yh.patient').sudo().create(kw)
       return request.render("theme_yourhome2.create_patient2", {})
