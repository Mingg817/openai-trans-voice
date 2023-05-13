import os

import whisper


def model(model):
    if (model is None):
        model = "small"
    model = whisper.load_model(model)
    current_dir = os.getcwd()
    file_list = [i for i in os.listdir(current_dir) if (i[0] != '.' and i[-4:] != '.txt')]
    for filename in file_list:
        result = model.transcribe(os.path.join(current_dir, filename), verbose=True)
        write_to_file(result.get("segments"), filename)
        print(f"Done! Located in {filename + '.txt'}")


def write_to_file(segments, filename):
    current_dir = os.getcwd()
    rett = open(os.path.join(current_dir, filename + ".txt"), "w")
    wls = []
    for t in segments:
        wls.append(t["text"].strip())
    wls2 = list(set(wls))
    wls2.sort(key=wls.index)
    rett.write("\n".join(wls2))
    rett.close()
