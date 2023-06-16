import re
import os
from dotenv import load_dotenv, find_dotenv


# get config variables from .env file
load_dotenv(find_dotenv())
MIN_QUOTE_LENGTH = int(os.getenv("MIN_QUOTE_LENGTH"))
MAX_QUOTE_LENGTH = int(os.getenv("MAX_QUOTE_LENGTH"))


# reads flat .txt. file and parses it into a list of dictionaries
# the key 'title' is the title of the book
# the key 'author' is the author of the book
# the key 'type' can be: Highlight, Note, Bookmark
# the key 'date added' is the date when the quote was highlighted by the reader
# the key 'quote' is the quote body
def parse_to_dict(filename):
    with open(filename, "r") as f:
        text = f.read()

    # Regex that searches for the following pattern
    pattern = r"(?P<title>.+?) \((?P<author>[^)]+)\)\n- Your (?P<type>Highlight|Note|Bookmark) on (?:page (?P<page>\d+|[ivxlcdm]+) \| )?Location (?P<location>\d+-\d+) \| Added on (?P<date_added>.+?)\n\n(?P<quote>[^\n]+)"

    # Searches for unique matches of the pattern within the text file
    matches = re.findall(pattern, text, re.MULTILINE)

    # Create a list of dictionaries, one for each match
    result = []

    # Use a loop to convert each tuple to a dictionary with the required keys and values
    for match in matches:
        title, author, htype, page, location, date_added, quote = match
        words = author.split(', ') # Split author string to ['Lastname', 'Firstname']
        author = words[1] + ' ' + words[0] #Replace Firstname with Lastname and conversely
        result.append(
            {
                "title": title,
                "author": author,
                "type": htype,
                "page": page,
                "location": location,
                "date_added": date_added,
                "quote": quote,
            }
        )
    return result


# Takes list of dictionaries and removes quotes that are too short, truncates quotes that are too long
def clean_list(my_list):
    # Create a new list to avoid changing while iterating
    cleaned_list = []

    for item in my_list:
        quote = item["quote"]
        quote_length = len(quote)
        if quote_length > MIN_QUOTE_LENGTH:
            if quote_length > MAX_QUOTE_LENGTH:
                truncated_quote = quote[:MAX_QUOTE_LENGTH].rsplit(" ", 1)[0] + " ..."
                item["quote"] = truncated_quote
            cleaned_list.append(item)
    return cleaned_list


# Takes list of dictionaries and removes duplicate quotes
# Addresses a Kindle bug: when the reader edits a highlight, it registers as a new highlight
# Current logic takes the quote that reflects the most recent edit
def deduplicate_list(my_list):
    new_list = []

    for i, quote1 in enumerate(my_list):
        is_duplicate = False

        for quote2 in my_list[i + 1 :]:
            # quotes are duplicates if they are a substring of each other, and are from the same book
            if (
                quote1["title"] == quote2["title"]
                and quote1["quote"] in quote2["quote"]
            ):
                is_duplicate = True

                # keep the most recent edit of the highlight by the reader
                if quote1["date_added"] <= quote2["date_added"]:
                    quote1 = quote2
                break

        if not is_duplicate:
            new_list.append(quote1)

    print("Number of quotes deduplicated: " + str(len(my_list) - len(new_list)))
    return new_list


# run only if this is the program being explicitly run
if __name__ == "__main__":
    print("You are only running" + __file__ + "and not importing it.")
