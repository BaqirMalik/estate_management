from odoo import fields, models

class PropertyUnits(models.Model):

	_name = "property.units"
	_description = "Property Units"
	_rec_name = 'title'

	title = fields.Char("Title")
	no_of_rooms = fields.Integer('Rooms')
	size = fields.Integer('Size')
	demand = fields.Float("Demand")
	final_price = fields.Float("Final Price")
	post_code = fields.Integer("Postal Code")
	description = fields.Text("Description")
	available_date = fields.Date("Available Date")
	area = fields.Float("Area")
	product_type = fields.Selection(string="Type", selection=[
		('house', 'House'),
		('office', 'Office'),
		('flat', 'Flat'),
		('plot', 'Plot')])
	state = fields.Selection(string="Status", selection=[
		('sold', 'Sold'),
		('freeze', 'Freeze'),
		('cancel', 'Cancel')])

	sales_person = fields.Many2one("res.partner", string="Sales Person")
	buyer = fields.Many2one("res.users", string="Buyer")
	latitude = fields.Float("Latitude", digits=(3, 6))
	longitude = fields.Float("Longitude", digits=(3, 6))


	def action_sale(self):
		self.state = 'sold'

	def action_freeze(self):
		self.state = 'freeze'

	def action_cancel(self):
		self.state = 'cancel'


