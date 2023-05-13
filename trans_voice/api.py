import os

import dotenv
import openai

dotenv.load_dotenv()


def api(prompt: str):
    os.environ["http_proxy"] = "http://127.0.0.1:8889"
    os.environ["https_proxy"] = "http://127.0.0.1:8889"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    current_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../inputs")
    file_list = os.listdir(current_dir)
    for filename in file_list:
        audio_file = open(os.path.join(current_dir, filename), "rb")
        config = {'file': audio_file,
                  'model': "whisper-1",
                  'response_format': 'verbose_json',
                  'prompt': prompt
                  }
        transcript = openai.Audio.transcribe(**config)
        write_to_file(transcript.segments, filename)
        print(f"Done! Located in {filename + '.txt'}")


def write_to_file(segments, filename):
    current_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../outputs")
    rett = open(os.path.join(current_dir, filename + ".txt"), "w")
    wls = []
    for t in segments:
        wls.append(t.text.strip())
    wls2 = list(set(wls))
    wls2.sort(key=wls.index)
    rett.write("\n".join(wls2))
    rett.close()
