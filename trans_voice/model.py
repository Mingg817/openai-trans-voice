import os

import whisper


def model(args):
    if (args.model is None):
        args.model = "small"
    model = whisper.load_model(args.model)
    current_dir = os.getcwd()
    file_list = [i for i in os.listdir(current_dir) if (i[0] != '.' and i[-4:] != '.txt')]
    for filename in file_list:
        result = model.transcribe(os.path.join(current_dir, filename), verbose=True)
        write_to_file(result.get("segments"), filename)
        print(f"Done! Located in {filename + '.txt'}")
    if args.combine:
        combine_files()


def write_to_file(segments, filename):
    current_dir = os.getcwd()
    rett = open(os.path.join(current_dir, filename + ".txt"), "w")
    wls = []
    for t in segments:
        wls.append(t["text"].strip())
    wls2 = list(set(wls))
    wls2.sort(key=wls.index)
    # 文件内用空格分割
    rett.write(" ".join(wls2))
    rett.close()


def combine_files():
    current_dir = os.getcwd()
    file_list = [i for i in os.listdir(current_dir) if i[-4:] == '.txt']
    with open('combined.txt', 'w') as outfile:
        for fname in file_list:
            with open(fname) as infile:
                for line in infile:
                    outfile.writelines([line, '\n'])
