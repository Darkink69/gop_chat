from gradio_client import Client, handle_file

def get_transcribe(audio):
	client = Client("n902/whisper")
	result = client.predict(
		audio=handle_file(audio),
		api_name="/predict"
	)
	print(result)
	return result

