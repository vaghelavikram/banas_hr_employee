from datetime import date
from odoo import api, fields, models

class BanasHrEmployee(models.Model):
    _inherit = "hr.employee"

    # name = fields.Char(string='Employee Name') 
    adhar_no = fields.Char(string='AAdhar No')
    sallary = fields.Integer(string='Salary')
    net_gross_sallary = fields.Integer(string='Net Gross Salary')
    didcution = fields.Integer(string='Diduction')

    