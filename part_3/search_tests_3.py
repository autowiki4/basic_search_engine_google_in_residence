from search import keyword_to_titles, title_to_info, search, article_length, key_by_author, filter_to_author, \
    filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main


class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(
            advanced_option) + '\n' + print_advanced_option(advanced_option) + str(
            advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    '''
    This test will verify if the program correctly filters articles 
    based on a maximum title length provided by the user.
    '''

    @patch('builtins.input')
    def test_article_title_length(self, input_mock):
        keyword = 'cartoon'
        advanced_option = 1
        max_title_length = 15

        # Mock user inputs
        # input_mock.side_effect = [keyword, advanced_option, max_title_length]

        # Expected output based on title length constraint
        expected = print_basic() + keyword + '\n' + print_advanced() + str(
            advanced_option) + '\n' + print_advanced_option(advanced_option) + str(
            max_title_length) + "\n\nHere are your articles: ['Spongebob']\n"

        # Run the function and check
        output = get_print(input_mock, [keyword, advanced_option, max_title_length])
        self.assertEqual(output, expected)

    '''
    This test will check if the program remaps articles 
    by author and lists all titles written by each relevant author.
    '''
    patch('builtins.input')

    def test_key_by_author(self, input_mock):
        keyword = 'Spongebob'
        advanced_option = 2

        # Mock user inputs
        # input_mock.side_effect = [keyword, advanced_option]

        # Expected output
        expected = print_basic() + keyword + '\n' + print_advanced() + str(
            advanced_option) + '\n' + print_advanced_option(
            advanced_option) + "\n\nHere are your articles grouped by author: {'Mr Jake': ['Spongebob - the legacy']}\n"

        # Run the function and check
        output = get_print(input_mock, [keyword, advanced_option])
        self.assertEqual(output, expected)

    '''
    This test will verify if the program correctly filters articles 
    to only include those written by a specified author.
    '''

    @patch('builtins.input')
    def test_filter_to_author(self, input_mock):
        keyword = 'tv'
        advanced_option = 3
        author = 'Mr Jake'

        # Mock user inputs
        # input_mock.side_effect = [keyword, advanced_option, author]

        # Expected output
        expected = print_basic() + keyword + '\n' + print_advanced() + str(
            advanced_option) + '\n' + print_advanced_option(
            advanced_option) + author + "\n\nHere are your articles: ['Spongebob - the legacy']\n"

        # Run the function and check
        output = get_print(input_mock, [keyword, advanced_option, author])
        self.assertEqual(output, expected)

    '''
    This test checks if the program excludes articles 
    that contain a specified keyword in their metadata.
    '''

    @patch('builtins.input')
    def test_filter_out_keyword(self, input_mock):
        keyword = 'cartoon'
        advanced_option = 4
        filter_out_keyword = 'pineapple'

        # Mock user inputs
        # input_mock.side_effect = [keyword, advanced_option, filter_out_keyword]

        # Expected output
        expected = print_basic() + keyword + '\n' + print_advanced() + str(
            advanced_option) + '\n' + print_advanced_option(
            advanced_option) + filter_out_keyword + "\n\nHere are your articles: []\n"

        # Run the function and check
        output = get_print(input_mock, [keyword, advanced_option, filter_out_keyword])
        self.assertEqual(output, expected)

    '''
    Notes on the Expected Output
    print_basic() and print_advanced() should format the
    user prompts as strings for each step in the user interaction flow.
    print_advanced_option(advanced_option) should return specific instructions based 
    on the advanced option selected.
    '''


# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()