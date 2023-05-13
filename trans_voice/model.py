import os
import whisper


def model(model):
    if (model is None):
        model = "small"
    model = whisper.load_model(model)
    current_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../inputs")
    file_list = os.listdir(current_dir)
    for filename in file_list:
        result = model.transcribe(os.path.join(current_dir, filename))
        write_to_file(result.get("segments"), filename)
        print(f"Done! Located in {filename + '.txt'}")


def write_to_file(segments, filename):
    current_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../outputs")
    rett = open(os.path.join(current_dir, filename + ".txt"), "w")
    wls = []
    for t in segments:
        wls.append(t["text"].strip())
    wls2 = list(set(wls))
    wls2.sort(key=wls.index)
    rett.write("\n".join(wls2))
    rett.close()
