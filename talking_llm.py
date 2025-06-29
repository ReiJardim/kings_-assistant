# Gravar voz
# De audio para texto - Wisper
# esse texto vai para uma llm  - Agents
# Respostas - TTS
import openai
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=api_key)


class TalkingLLM:

    def __init__(self):
        pass

    def strat_or_stop_recording(self):
        pass

    def create_agent(self):
        pass

    def save_and_transcribe(self):
        pass

    def convert_and_play(self):
        pass

    def run(self):
        print("KKKKKKKK Vou dominar o mundo")
        pass


if __name__ == "__main__":
    talking_llm = TalkingLLM()
    talking_llm.run()
