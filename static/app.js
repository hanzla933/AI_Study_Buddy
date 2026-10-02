"use strict";

const form = document.querySelector("#pdf-form");
const fileInput = document.querySelector("#pdf-file");
const status = document.querySelector("#status");
const output = document.querySelector("#extracted-text");

form.addEventListener("submit", async (event) => {
	event.preventDefault();
	const file = fileInput.files[0];
	if (!file) return;

	const formData = new FormData();
	formData.append("file", file);
	status.textContent = "Extracting text...";
	output.hidden = true;

	try {
		const response = await fetch("/api/documents/extract", {
			method: "POST",
			body: formData,
		});
		const result = await response.json();
		if (!response.ok) throw new Error(result.detail || "Could not read this PDF.");

		output.textContent = result.text || "No selectable text found in this PDF.";
		output.hidden = false;
		status.textContent = `Extracted text from ${result.filename}.`;
	} catch (error) {
		status.textContent = error.message;
	}
});
