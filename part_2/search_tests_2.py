from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    METADATA = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ], ['1922 in music', 'Gary King', 1242717698, 11576]]

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    # test for search function
    def test_search(self):
        # Test case for search function
        self.assertEqual(search("personality"), [
            ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023]
        ])

        self.assertEqual(search("production"), [
            ['1922 in music', 'Gary King', 1242717698, 11576], ['1936 in music', 'RussBot', 1243745950, 23417], ['Annie (musical)', 'Jack Johnson', 1223619626, 27558], ['The Hunchback of Notre Dame (musical)', 'Nihonjoe', 1192176615, 42]
        ])

        self.assertEqual(search(""), []) # No keyword provided, should return empty list


    # test for article_length function
    def test_article_length(self):
        # Test case for article_length function
        self.assertEqual(article_length(9000, self.METADATA), [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526]])

        self.assertEqual(article_length(10000, self.METADATA), [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526]])

        self.assertEqual(article_length(2000, self.METADATA), []) # No article within 2000 characters


    # test for unique_authors function
    def test_unique_authors(self):
        # Test case for unique_authors function
        self.assertEqual(unique_authors(1, self.METADATA), [
            ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023]
        ])

        self.assertEqual(unique_authors(3, self.METADATA), [
            ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023],
            ['1922 in music', 'Gary King', 1242717698, 11576]
        ])

        self.assertEqual(unique_authors(10, self.METADATA), [
            ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023],
            ['1922 in music', 'Gary King', 1242717698, 11576]
        ])  # count larger than unique authors, returns all unique


    # test for most_recent_article function
    def test_most_recent_article(self):
        # Test case for most_recent_article function
        self.assertEqual(most_recent_article(self.METADATA), [
            '1922 in music', 'Gary King', 1242717698, 11576
        ])

        self.assertEqual(most_recent_article([['Article', 'Author', 1234567890, 100]]), [
            'Article', 'Author', 1234567890, 100
        ])  # Single article, should return it

        self.assertEqual(most_recent_article([]), [])  # Empty list should return empty result


    # test for favorite_author function
    def test_favorite_author(self):
        # Test case for favorite_author function
        self.assertEqual(favorite_author("Jack Johnson", self.METADATA), True)
        self.assertEqual(favorite_author("GARY KING", self.METADATA), True) # Case-insensitive
        self.assertEqual(favorite_author("Unknown Author", self.METADATA), False)


    # test for title_and_author function
    def test_title_and_author(self):
        # Test case for title_and_author function
        self.assertEqual(title_and_author(self.METADATA), [
            ('List of Canadian musicians', 'Jack Johnson'),
            ('Edogawa, Tokyo', 'jack johnson'),
            ('1922 in music', 'Gary King')
        ])

        self.assertEqual(title_and_author([]), [])  # Empty list should return empty result

        self.assertEqual(title_and_author([['A', 'B', 1234, 100]]), [
            ('A', 'B')
        ]) # Single article, should return one tuple


    # test for refine_search function
    def test_refine_search(self):
        # Test case for refine_search function
        self.assertEqual(refine_search("personality", search("johnson")), [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023]])
        self.assertEqual(refine_search("missing", search("nonexistent")), [])  # No matches found

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    # Integration test for advanced option #1 (Article Length)
    @patch('builtins.input')
    def test_integration_article_length(self, input_mock):
        keyword = 'science'
        advanced_option = 1
        max_length = 2500

        output = get_print(input_mock, [keyword, advanced_option, max_length])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + \
                   print_advanced_option(advanced_option) + str(max_length) + f"\n\nHere are your articles: [['Embryo drawing', 'Jack Johnson', 1034459202, 1712]]\n"
        self.assertEqual(output, expected)

    # Integration test for advanced option #2 (Unique Authors)
    @patch('builtins.input')
    def test_integration_unique_authors(self, input_mock):
        keyword = 'technology'
        advanced_option = 2
        unique_author_count = 3

        output = get_print(input_mock, [keyword, advanced_option, unique_author_count])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + \
                   print_advanced_option(advanced_option) + str(unique_author_count) + f"\n\nHere are your articles: [['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Digital photography', 'Mr Jake', 1095727840, 18093]]\n"
        self.assertEqual(output, expected)

    # Integration test for advanced option #3 (Most Recent Article)
    @patch('builtins.input')
    def test_integration_most_recent_article(self, input_mock):
        keyword = 'AI'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + \
                   print_advanced_option(advanced_option) + f"\nNo articles found\n"
        self.assertEqual(output, expected)

    # Integration test for advanced option #4 (Favorite Author)
    @patch('builtins.input')
    def test_integration_favorite_author(self, input_mock):
        keyword = 'health'
        advanced_option = 4
        favorite_author = 'Dr. John Doe'

        output = get_print(input_mock, [keyword, advanced_option, favorite_author])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + \
                   print_advanced_option(advanced_option) + favorite_author + "\n\nHere are your articles: [['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582]]\nYour favorite author is not in the returned articles!\n"
        self.assertEqual(output, expected)

    # Integration test for advanced option #5 (Title and Author)
    @patch('builtins.input')
    def test_integration_title_and_author(self, input_mock):
        keyword = 'economics'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + \
                   print_advanced_option(advanced_option) + "\nNo articles found\n"
        self.assertEqual(output, expected)

    # Integration test for advanced option #6 (Refine Search)
    @patch('builtins.input')
    def test_integration_refine_search(self, input_mock):
        keyword = 'machine learning'
        advanced_option = 6
        refine_keyword = 'deep learning'

        output = get_print(input_mock, [keyword, advanced_option, refine_keyword])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + \
                   print_advanced_option(advanced_option) + refine_keyword + "\n\nNo articles found\n"
        self.assertEqual(output, expected)

    # Integration test for advanced option #7 (No Additional Filters)
    @patch('builtins.input')
    def test_integration_no_advanced_option(self, input_mock):
        keyword = 'biology'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + \
                   "\nHere are your articles: [['Embryo drawing', 'Jack Johnson', 1034459202, 1712]]\n"
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()