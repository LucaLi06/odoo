from odoo import http
from odoo.http import request


class Hospital(http.Controller):

    @http.route('/patient_webform/', type="http",auth="public",website="true")
    def patient_webform(self,**kw):
        return http.request.render('theme_haemertest.create_patient',{})

    @http.route('/create/webpatient/', type="http",auth="public",website="true")
    def create_webpatient(self,**kw):
        patient = request.env['haemer.patient'].sudo().create({
            'name': kw.get('name'),
        })
        vals = {
            'patient': patient,
        }
        return request.render("theme_haemertest.create_patient", vals)
