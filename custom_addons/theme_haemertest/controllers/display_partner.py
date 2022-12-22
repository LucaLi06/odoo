from odoo import http


class HaemerTestPartner(http.Controller):

    @http.route('/partners/', auth="public", type="json", methods=['POST'])
    def all_partners(self):
        partners = http.request.env['haemer.partner'].search_read([], ['name', 'url', 'image'])
        return partners