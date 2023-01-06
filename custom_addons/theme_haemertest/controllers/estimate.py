from odoo import http
from odoo.http import request
from odoo import fields


class Estimate(http.Controller):

    @http.route('/estimate_webform/', type="http",auth="public",website="true")
    def patient_webform(self,**kw):
        return http.request.render('theme_haemertest.create_estimate',{})

    @http.route('/create/estimate/', type="http",auth="public",website="true")
    def create_estimate(self, **kw):
        selection = fields.Selection([('soil', 'soil'), ('choice2', 'choice2'), ('choice3', 'choice3')])
        print("------", selection)
        estimate = request.env['haemer.estimate'].sudo().create({
            'enterprise': kw.get('enterprise'),
            'name': kw.get('name'),
            'address': kw.get('address'),
            'latitude': kw.get('latitude'),
            'longitude': kw.get('longitude'),
            'past_activity': kw.get('past_activity'),
            'future_activity': kw.get('future_activity'),
            'remediation_type': kw.get('remediation_type'),
            'volume': kw.get('volume'),
            'density': kw.get('density'),
            'humidity': kw.get('humidity'),
            'porosity': kw.get('porosity'),
        })
        print("-------",kw)

        return request.render("theme_haemertest.create_estimate", {'selection': selection})
