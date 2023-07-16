import argparse
import os

from trans_voice.api import api
from trans_voice.model import model

print(os.path.abspath(__file__))

parser = argparse.ArgumentParser(
    prog="python -m trans_voice"
)

group = parser.add_mutually_exclusive_group()
group.add_argument("-a", "--api", action="store_true", help="Use OpenAI api. Can not over 25M.")
group.add_argument("-l", "--local", action="store_true", help="Use local Whisper Model")
parser.add_argument("-p", "--prompt", metavar="", type=str, help="input your prompt")
parser.add_argument("-m", "--model", metavar="", type=str, help="choice your model")
# 0.2 版本 - 添加输出文件一键合并功能
parser.add_argument("-c", "--combine", action="store_true", help="combine your outputs")

args = parser.parse_args()

if __name__ == '__main__':

    if args.api:
        print("Using api")
        api(args)
    elif args.local:
        print("Using model")
        model(args)
    else:
        parser.print_help(file=None)
