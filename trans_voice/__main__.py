import argparse
import os

from trans_voice.api import api
from trans_voice.model import model

print(os.path.abspath(__file__))

parser = argparse.ArgumentParser(
    prog="python -m trans_voice"
)

group = parser.add_mutually_exclusive_group()
# inGroup = parser.add_argument_group()
# inGroup.add_argument("-a", "--api", action="store_true", help="Use OpenAI api. Can not over 25M.")
# inGroup.add_argument("-p", "--prompt", type=str, help="input your prompt")
group.add_argument("-a", "--api", action="store_true", help="Use OpenAI api. Can not over 25M.")
group.add_argument("-l", "--local", action="store_true", help="Use local Whisper Model")
parser.add_argument("-p", "--prompt", metavar="", type=str, help="input your prompt")
parser.add_argument("-m", "--model", metavar="", type=str, help="choice your model")

args = parser.parse_args()

if __name__ == '__main__':

    if args.api:
        print("Using api")
        api(args.prompt)
    elif args.local:
        print("Using model")
        model(args.model)
    else:
        parser.print_help(file=None)
