import frappe
import openai
from frappe import _


@frappe.whitelist()
def transcribe_audio():
	"""
	Receives audio from the frontend, transcribes it using Whisper, and returns the result.
	"""
	# Fetch the audio file from the request
	audio_file = frappe.local.request.files.get("audio_file")
	if not audio_file:
		frappe.throw(_("No audio file received."))

	# Fetch API Key from System Settings
	api_key = frappe.db.get_single_value("System Settings", "openai_api_key")
	if not api_key:
		frappe.throw(_("OpenAI API key is not set in System Settings."))

	openai.api_key = api_key

	# Transcribe using Whisper
	try:
		response = openai.Audio.transcribe("whisper-1", audio_file)
		return response.get("text", _("No transcription available."))
	except Exception as e:
		frappe.log_error(frappe.get_traceback(), _("Whisper API Error"))
		frappe.throw(_("Error in transcription: {0}").format(str(e)))
