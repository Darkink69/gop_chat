from gradio_client import Client, handle_file

def get_transcribe():
	client = Client("openai/whisper")
	result = client.predict(
		inputs=handle_file('https://cdn0.101.ru/vardata/modules/musicdb/files/202006/23/be94d858ce16d331198d51b4cb95e966.mp3'),
		task="transcribe",
		api_name="/predict"
	)
	print(result)
	return result


