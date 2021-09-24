import json
import jsbeautifier
from rich.console import Console


class PrintUtils:
    def __init__(self):
        pass

    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    console = Console()

    @staticmethod
    def print_json(data, msg=None, type=None):
        options = jsbeautifier.default_options()
        options.indent_size = 2
        if msg is not None:
            if type == 'list':
                print(
                    f"{PrintUtils.OK}{msg}{PrintUtils.RESET}:  {jsbeautifier.beautify(json.dumps(list(data)), options)}")
            else:
                print(f"{PrintUtils.OK}{msg}{PrintUtils.RESET}:  {jsbeautifier.beautify(json.dumps(data), options)}")
        else:
            if type == 'list':
                print(f"{jsbeautifier.beautify(json.dumps(list(data)), options)}")
            else:
                print(f"{jsbeautifier.beautify(json.dumps(data), options)}")

    @staticmethod
    def print_yellow(msg):
        print(f"{PrintUtils.WARNING}{msg}{PrintUtils.RESET}")

    @staticmethod
    def print_green(msg):
        print(f"{PrintUtils.OK}{msg}{PrintUtils.RESET}")

    @staticmethod
    def print_red(msg):
        print(f"{PrintUtils.FAIL}{msg}{PrintUtils.RESET}")

    @staticmethod
    def print_log(msg, test_data):
        print(f"{PrintUtils.FAIL}{msg}{PrintUtils.RESET}")
        PrintUtils.console.log(test_data, log_locals=False)
