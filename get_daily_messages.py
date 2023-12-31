from imessage_reader import fetch_data
import sys
import subprocess
DB_PATH = "/Users/avikgarg/Library/Messages/chat.db"
SCRIPT_PATH = "/Users/avikgarg/Desktop/projects/time_management_sheet/new_entry.sh"

def get_date(message):
    return message[2][:10]
def get_sender(message):
    return message[0]
def get_words(message):
    return message[1].split()

fd = fetch_data.FetchData(DB_PATH)
messages = fd.get_messages()

#When you send yourself a message, 2 show up, so this avoids that
skipNext = False
for message in messages:
    if (skipNext):
        skipNext = False
        continue
    skipNext = False
    if (get_date(message) == sys.argv[1] and get_sender(message) == '+16123835311'):
        print([SCRIPT_PATH] + get_words(message))
        subprocess.run([SCRIPT_PATH] + get_words(message),capture_output=True, text=True)
        skipNext = True
