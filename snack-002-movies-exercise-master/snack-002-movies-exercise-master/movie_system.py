import random

Directors = ["Steven Spielberg", "Christopher Nolan", "Martin Scorsese", 
            "Quentin Tarantino", "Alfred Hitchcock", "Stanley Kubrick",
            "Francis Ford Coppola", "James Cameron", "Spike Lee", "Kathryn Bigelow"]

# TODO: Step 1 - Complete this function to:
# - Return the user_input if it's not empty
# - Return "movies.txt" if user_input is empty
# - Function must pass test_1_choose_movie_file and test_2_choose_movie_file_blank_input
def ask_file_name(user_input):
    pass

# TODO: Step 2 - Complete this function to:
# - Open and read the contents of file_name
# - Print "Loading director quotes database...\n" when successful
# - Handle FileNotFoundError and print appropriate error message
# - Return file contents as string when successful, empty string on error
# - Function must pass test_3_file_not_found and test_4_file_successfully_opened
def read_file(file_name):
    pass

# TODO: Step 3 - Complete this function to:
# - Use random.choice() to select a random director from the Directors list
# - Return the selected director
# - Function must pass test_5_choose_random_director
def select_random_director(Directors):
    pass

# TODO: Step 4 - Complete this function to:
# - Search through movies list for quotes by random_director
# - Extract quote and year from matching entry
# - Format should match "Director ~ Quote | Year" from movies.txt
# - Return "Director not found in database." if director has no quotes
# - Function must pass test_6_find_movie_quote_with_year
def find_movie_quote(random_director, movies):
    pass

# TODO: Step 5 - Print the quote in a cinematic format with separators and year
def display_movie_quote(quote_data, director):
    if "|" not in quote_data:
        print("Invalid quote format")
        return
    
    quote, year = quote_data.split("|")
    print("\n" + "="*50)
    print(f"Director Spotlight: {director}")
    print(f"Year: {year.strip()}")
    print("-"*50)
    print(f"Quote: {quote.strip()}")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("🎬 Welcome to Director's Cut - Famous Movie Quotes 🎬\n")
    user_input = input("Enter quotes database file [press Enter for movies.txt]: ")
    movies_file = ask_file_name(user_input)
    print(f"\nUsing database: {movies_file}\n")
    
    movies = read_file(movies_file).split("\n\n")
    random_director = select_random_director(Directors)
    
    if random_director == "":
        print('Error: Director list is empty.\n')
    else:
        print(f"🎥 Selected Director: {random_director}\n")
    
    quote_data = find_movie_quote(random_director, movies)
    if "not found" in quote_data:
        print(f"❌ {random_director}'s quotes are not available in the database.\n")
        quit()
    else:
        display_movie_quote(quote_data, random_director)
