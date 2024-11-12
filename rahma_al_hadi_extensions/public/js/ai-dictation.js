frappe.ui.form.on("AI Dictation Test", {
	refresh: function (frm) {
		frm.add_custom_button(__("Start Voice Transcription"), function () {
			// Check if the browser supports MediaRecorder
			if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
				frappe.msgprint(__("Your browser does not support audio recording."));
				return;
			}

			// Request microphone permission and start recording
			navigator.mediaDevices
				.getUserMedia({ audio: true })
				.then((stream) => {
					const mediaRecorder = new MediaRecorder(stream);
					const audioChunks = [];

					frappe.msgprint(__("Recording started. Click 'Stop Recording' to finish."));

					mediaRecorder.ondataavailable = (event) => {
						audioChunks.push(event.data);
					};

					mediaRecorder.onstop = () => {
						const audioBlob = new Blob(audioChunks, { type: "audio/webm" });

						// Send the audio to the server
						const formData = new FormData();
						formData.append("audio_file", audioBlob, "recording.webm");

						frappe.call({
							method: "rahma_al_hadi_extensions.rahma_al_hadi_extensions.api.transcribe_audio",
							args: {},
							headers: {
								"X-Frappe-CSRF-Token": frappe.csrf_token,
							},
							type: "POST",
							contentType: false,
							processData: false,
							data: formData,
							callback: function (r) {
								if (r.message) {
									frm.set_value("transcription", r.message);
									frappe.msgprint(__("Transcription completed!"));
								}
							},
							error: function () {
								frappe.msgprint(__("Error in transcription."));
							},
						});
					};

					// Start recording
					mediaRecorder.start();

					// Add a button to stop the recording
					frm.add_custom_button(__("Stop Recording"), function () {
						mediaRecorder.stop();
						frappe.msgprint(__("Recording stopped. Processing transcription..."));
					});
				})
				.catch((err) => {
					frappe.msgprint(__("Microphone access denied or error occurred."));
					console.error(err);
				});
		});
	},
});
