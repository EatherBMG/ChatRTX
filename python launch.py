class MyModel:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def create_response(self, text_str: str, prompt_length: int, completion_length: int) -> CompletionResponse:
        # Dies erstellt und gibt eine Antwortstruktur für das KI-Modell zurück
        response = {
            "model": self.model_name,
            "choices": [
                {
                    "text": text_str,
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": 'stop'
                }
            ],
            "usage": {
                "prompt_tokens": prompt_length,
                "completion_tokens": completion_length,
                "total_tokens": prompt_length + completion_length
            }
        }
        return response

    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        # Hier wird der Antworttext generiert und zurückgegeben
        generated_text = "This is the generated response based on the prompt: " + prompt
        prompt_length = len(prompt.split())
        completion_length = len(generated_text.split())
        return self.create_response(generated_text, prompt_length, completion_length)

my_model = MyModel(model_name="MySuperModel")
# Ein Beispiel-Prompt
prompt = "Was ist der Sinn des Lebens?"

# Interagiere mit der KI
response = my_model.stream_complete(prompt)
print(response)
