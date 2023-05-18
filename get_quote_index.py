import os


# Simple function that increments the index of the list by one
# Stored in peristent memory (e.g. counter.txt) to keep track of index between runs
def get_simple_index(list_length):
    pwd_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(pwd_path, "counter.txt")
    
    # If the counter.txt file does not exist, create it and set the counter to 0
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")
        cur_count = 0
    
    else:
        try:
            with open(file_path, "r") as f:
                cur_count = int(f.readline().strip())
        except ValueError as ve:
            print(f"Exception: Counter.txt does not contain a valid integer. Type: {ve}")
            cur_count = 0
            print("Resetting counter.txt to " + str(cur_count))

    # If the counter reaches the end of the list, reset it to the beginning
    if cur_count >= list_length or cur_count < 0:
        cur_count = 0

    # Increment the counter each time that the method is called
    next_count = cur_count + 1

    # Update the counter value in the counter.txt file
    with open(file_path, "w") as f:
        f.write(str(next_count))

    return cur_count


if __name__ == "__main__":
    print("You are only running" + __file__ + "and not importing it.")
