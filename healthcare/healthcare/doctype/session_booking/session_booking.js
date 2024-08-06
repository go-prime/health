// Copyright (c) 2024, healthcare and contributors
// For license information, please see license.txt

frappe.ui.form.on('Session Booking', {
	// refresh: function(frm) {

	// }
	patient: function(frm){
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Patient",
				name: cur_frm.doc.patient,
			},
			callback(r) {
				if(r.message) {
					frm.set_value("first_name", r.message.first_name);
					frm.set_value("last_name",  r.message.last_name);
					frm.set_value("gender",  r.message.sex);	
				}
			}
		});
		

	}
});
