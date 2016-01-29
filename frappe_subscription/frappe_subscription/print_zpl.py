import frappe

@frappe.whitelist()
def print_zpl(docname):
	frappe.errprint(docname)
	return None