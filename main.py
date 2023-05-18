import os
from dotenv import load_dotenv, find_dotenv
import datetime
import parse_txt_file
import get_quote_index
import sms_sender

# get the file path to the Kindle .txt file
load_dotenv(find_dotenv())
my_file = os.getenv("TXT_FILE")


def main():
    try:
        # Print to console each time this program is run
        # If running through launchd, will print to stdout.log instead
        print("This program was run at: " + str(datetime.datetime.now()))

        # Parses .txt file into a list of dictionaries (each quote is a dict)
        original_list = parse_txt_file.parse_to_dict(my_file)
        cleaned_list = parse_txt_file.clean_list(original_list)
        deduplicated_list = parse_txt_file.deduplicate_list(cleaned_list)
        final_list = list(deduplicated_list)
        
        list_length = len(final_list)
        print("Total quotes: " + str(list_length))

        # Get the index of the quote to send
        quote_index = get_quote_index.get_simple_index(list_length)

        # Get the quote body from the dict
        quote_body = final_list[quote_index]["quote"]

        # Construct message body that Twilio will deliver
        # Print statement is for testing purposes only
        msg = (
            "Today's quote is at index " + str(quote_index) + ":\n\n" + str(quote_body)
        )
        print(msg)

        # Invoke the Twilio SMS service
        sms_sender.send_sms(msg)

    except FileNotFoundError as fnfe:
        print(f"Exception: File from .env was not found: {fnfe.filename}")
    except Exception as other_error:
        print(f"Exception: There was an other error in main(): {other_error}")


if __name__ == "__main__":
    main()
