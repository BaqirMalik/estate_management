from odoo import fields, models

class EstateProperties(models.Model):

	_name = "estate.property"
	_description = "Real-Estate Properties"
	_rec_name = 'name'

	name = fields.Char("Name", required=True)
	description = fields.Text("Description")
	partner_id = fields.Many2one("res.partner", string="Partner")
	available_date = fields.Date("Available Date")
	active = fields.Boolean("Active")

	state = fields.Selection(string="Status", selection=[
		('draft', 'Draft'),
		('pending', 'Pending'),
		('accepted', 'Accepted'),
		('rejected', 'Rejected'),
		('cancelled', 'Cancelled'),
		('done', 'Done')], default='draft')

	def action_submit(self):
		self.state = 'pending'
	def action_accepted(self):
		self.state = 'accepted'

	def action_rejected(self):
		self.state = 'rejected'

	def action_cancelled(self):
		self.state = 'cancelled'

	def action_done(self):
		self.state = 'done'

	def action_draft(self):
		self.state = 'draft'