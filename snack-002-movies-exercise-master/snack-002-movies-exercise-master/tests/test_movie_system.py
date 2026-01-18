import unittest
from io import StringIO
import sys
from unittest.mock import patch
import movie_system

class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("\n"))
    def test_1_choose_movie_file(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertEqual(movie_system.ask_file_name('movies.txt'), "movies.txt")
    
    @patch("sys.stdin", StringIO("\n"))
    def test_2_choose_movie_file_blank_input(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertEqual(movie_system.ask_file_name(''), "movies.txt")
      
    def test_3_file_not_found(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        movie_system.read_file("mock.txt")
        self.assertEqual("""Database Error: File 'mock.txt' not found.\n""", text_capture.getvalue())

    def test_4_file_successfully_opened(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        movie_system.read_file("movies.txt")
        self.assertEqual("""Loading director quotes database...\n\n""", text_capture.getvalue())
        self.assertEqual(type(movie_system.read_file("movies.txt")), str)

    def test_5_choose_random_director(self):
        self.assertEqual(movie_system.select_random_director(["Steven Spielberg"]), "Steven Spielberg")

    def test_6_find_movie_quote_with_year(self):
        test_quote = "Christopher Nolan -> \"The Dark Knight is about fighting fear with fear.\" | 2008"
        self.assertEqual(
            movie_system.find_movie_quote("Christopher Nolan", [test_quote]),
            "\"The Dark Knight is about fighting fear with fear.\" | 2008"
        )

    def test_7_display_formatting(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        movie_system.display_movie_quote("\"Test quote\" | 2000", "Test Director")
        expected_output = "\n==================================================\n" + \
                         "Director Spotlight: Test Director\n" + \
                         "Year: 2000\n" + \
                         "--------------------------------------------------\n" + \
                         "Quote: \"Test quote\"\n" + \
                         "==================================================\n\n"
        self.assertEqual(text_capture.getvalue(), expected_output)

    # Negative Tests
    def test_8_empty_directors_list(self):
        self.assertEqual(movie_system.select_random_director([]), "")

    def test_9_invalid_file_path(self):
        self.assertEqual(movie_system.read_file("../invalid/path/movies.txt"), "")

    def test_10_director_not_in_database(self):
        test_quotes = ["Steven Spielberg -> \"Quote 1\" | 2000", 
                      "Christopher Nolan -> \"Quote 2\" | 2008"]
        self.assertEqual(
            movie_system.find_movie_quote("Martin Scorsese", test_quotes),
            "Director not found in database."
        )

    def test_11_malformed_quote_format(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        movie_system.display_movie_quote("Invalid quote format", "Test Director")
        self.assertEqual("Invalid quote format\n", text_capture.getvalue())

    def test_12_none_input_handling(self):
        self.assertEqual(movie_system.ask_file_name(None), "movies.txt")
        self.assertEqual(movie_system.find_movie_quote(None, []), "Director not found in database.")
        self.assertEqual(movie_system.select_random_director(None), "")

    def test_13_empty_movies_list(self):
        self.assertEqual(
            movie_system.find_movie_quote("Christopher Nolan", []),
            "Director not found in database."
        )

    def test_14_malformed_quote_entry(self):
        malformed_quotes = [
            "Invalid format",
            "Director with no arrow",
            "Director -> No year",
            "Director -> \"Quote\" | invalid_year"
        ]
        self.assertEqual(
            movie_system.find_movie_quote("Director", malformed_quotes),
            "Director not found in database."
        )

if __name__ == '__main__':
    unittest.main()
