from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property.type"
    _description = "This is the description of the estate property type model."

    name = fields.Char('Name', required=True)    