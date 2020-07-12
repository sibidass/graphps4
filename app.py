from freight.freight_ops import Freight_Booking
import os
import configparser
from helpers.reader import read_prompts

config = configparser.ConfigParser()

APP_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(APP_DIR, "inputPS4.txt")
OUTPUT_FILE = os.path.join(APP_DIR, "outputPS4.txt")
PROMPTS_FILE = os.path.join(APP_DIR, "promptsPS4.txt")
CONFIG_FILE = os.path.join(APP_DIR, "helpers", "templates.ini")

def start_operation(file, freight):
    op_list = read_prompts(file)
    for op in op_list:
        searcg_tag = op.split(":")[0]
        if searcg_tag == "searchTransportHub":
            freight.displayTransportHub()
        elif searcg_tag == "searchTrain":
            train_no = op.split(":")[1].strip()
            freight.displayConnectedCities(train_no)
        elif searcg_tag == "searchCities":
            src = op.split(":")[1].strip()
            dest = op.split(":")[2].strip()
            freight.displayDirectTrain(src, dest)
        elif searcg_tag == "ServiceAvailability":
            src = op.split(":")[1].strip()
            dest = op.split(":")[2].strip()
            freight.findServiceAvailable(src, dest)
        else:
            print("Unidentified operation")


if __name__ == '__main__':
    f = Freight_Booking(output_file=OUTPUT_FILE)
    f.readCityTrainfile(INPUT_FILE)
    f.showAll()
    start_operation(PROMPTS_FILE, f)
