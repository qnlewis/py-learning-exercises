import random

Quotees = ["Abdullah Ibrahim","Miriam Makeba", "Nelson Mandela", "Eleanor Roosevelt",
 "Anne Frank", "Alexander Graham Bell","Thomas Edison","Estee Lauder","Maya Angelou", "Walt Disney"]


def ask_file_name(user_input):
    if user_input:
        quotes_file = user_input
    else:
        quotes_file = "quotes.txt"
    return quotes_file

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print("File successfully opened...\n")
            return file.read()
    except FileNotFoundError as e:
        print("FileNotFoundError successfully handled")
        print(e)

def select_random_quotee(quotees):
    random_quotee = random.choice(quotees)
    return random_quotee

def find_quote(quotee, quotes):
    for quote in quotes:
        if isinstance(quote, str) and quote.startswith(quotee):
            return quote
    return "Quote/quotee does not exist."


def final_output(quote, quotee):
    quote_parts = str(quote).split("~")
    if len(quote_parts) > 1:
        print(f"{quotee}: \"{quote_parts[1].strip()}\"")
    else:
        print("Invalid quote format.")
 
 
if __name__ == "__main__":
    """
     You can leave this code as is, and only implemented above where the code comments prompt you.
     """
    user_input = input("Desired file? [leave empty to use quotes.txt] :")
    quotes_file = ask_file_name(user_input)
    print(repr(str(quotes_file)) + ': is your chosen file.\n')
    quotes = [quote.strip() for quote in read_file(quotes_file).split("\n\n")]
    random_quotee = select_random_quotee(Quotees)
    if random_quotee == "":
        print('Empty list.\n')
    else:
        print(str(random_quotee) + ' has randomly been chosen.\n')
    true_quote = find_quote(random_quotee,quotes)
    if true_quote == "":
        print(str(random_quotee) + ' is not present in the file\n')
        quit()
    else:
        print(str(random_quotee) + ' is present in the file\n')
        final_output(true_quote,random_quotee)