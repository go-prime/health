from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _(
			"This is based on transactions against this Patient. See timeline below for details"
		),
		"fieldname": "patient",
		"non_standard_fieldnames": {"Payment Entry": "party"},
		"transactions": [
			{
				"label": _("Appointments and Encounters"),
				"items": ["Patient Appointment", "Vital Signs"],
			},
			{"label": _("Lab Tests and Vital Signs"), "items": ["Lab Test"]},
			{"label": _("Billing and Payments"), "items": ["Sales Invoice", "Payment Entry"]},
		],
	}
