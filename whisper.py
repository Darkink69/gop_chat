from gradio_client import Client, handle_file

def get_transcribe(audio):
	client = Client("n902/whisper")
	result = client.predict(
		audio=handle_file(audio),
		api_name="/predict"
	)
	print(result)
	return result

# get_transcribe('https://cdn2.101.ru/vardata/modules/musicdb/files/202006/23/db5829042eec86c7212092eb8f84fe59.mp3')