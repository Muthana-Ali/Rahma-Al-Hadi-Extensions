app_name = "rahma_al_hadi_extensions"
app_title = "Rahma Al Hadi Extensions"
app_publisher = "MuthanaIT"
app_description = "Extensions for Al-Hadi Center for Frappe."
app_email = "muthanaali@warithit.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "rahma_al_hadi_extensions",
# 		"logo": "/assets/rahma_al_hadi_extensions/logo.png",
# 		"title": "Rahma Al Hadi Extensions",
# 		"route": "/rahma_al_hadi_extensions",
# 		"has_permission": "rahma_al_hadi_extensions.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rahma_al_hadi_extensions/css/rahma_al_hadi_extensions.css"
# app_include_js = "/assets/rahma_al_hadi_extensions/js/rahma_al_hadi_extensions.js"

# include js, css files in header of web template
# web_include_css = "/assets/rahma_al_hadi_extensions/css/rahma_al_hadi_extensions.css"
# web_include_js = "/assets/rahma_al_hadi_extensions/js/rahma_al_hadi_extensions.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rahma_al_hadi_extensions/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "rahma_al_hadi_extensions/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "rahma_al_hadi_extensions.utils.jinja_methods",
# 	"filters": "rahma_al_hadi_extensions.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rahma_al_hadi_extensions.install.before_install"
# after_install = "rahma_al_hadi_extensions.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rahma_al_hadi_extensions.uninstall.before_uninstall"
# after_uninstall = "rahma_al_hadi_extensions.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "rahma_al_hadi_extensions.utils.before_app_install"
# after_app_install = "rahma_al_hadi_extensions.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "rahma_al_hadi_extensions.utils.before_app_uninstall"
# after_app_uninstall = "rahma_al_hadi_extensions.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rahma_al_hadi_extensions.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rahma_al_hadi_extensions.tasks.all"
# 	],
# 	"daily": [
# 		"rahma_al_hadi_extensions.tasks.daily"
# 	],
# 	"hourly": [
# 		"rahma_al_hadi_extensions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rahma_al_hadi_extensions.tasks.weekly"
# 	],
# 	"monthly": [
# 		"rahma_al_hadi_extensions.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "rahma_al_hadi_extensions.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rahma_al_hadi_extensions.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rahma_al_hadi_extensions.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["rahma_al_hadi_extensions.utils.before_request"]
# after_request = ["rahma_al_hadi_extensions.utils.after_request"]

# Job Events
# ----------
# before_job = ["rahma_al_hadi_extensions.utils.before_job"]
# after_job = ["rahma_al_hadi_extensions.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"rahma_al_hadi_extensions.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

