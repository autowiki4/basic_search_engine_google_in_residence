from wiki import article_titles, ask_search, ask_advanced_search


# 1)
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article titles
#
# Returns: list of article titles containing given keyword (case insensitive).
# If the keyword is empty or no results are found, return an empty list.
#
# Hint: to get list of existing article titles, use article_titles()
def search(keyword):
    # convert all characters of the keyword to lower case
    insesitive_keyword = keyword.lower()

    # list to contain the articles that meet the condition
    article_keyword = []

    for article in wiki.article_titles():
        # convert all characters of the article name to lower case
        insesitive_article = article.lower()
        if insesitive_keyword in insesitive_item:
            article_keyword.append(article)  # append article to list

    # return the article
    return article_keyword


# 2)
#
# Function: title_length
#
# Returns
#
# Parameters:
#   max_length - max character length of article titles
#   titles - list of article titles to search through
#
# Returns: list of article titles from given titles with a length that does
# not exceed max_length number of characters
def title_length(max_length, titles):
    # list to contain articles which meet the required length
    precise_articles = []

    for article in titles:
        # append the article if it mees the required length criteria
        if len(article) <= max_length:
            precise_articles.append(article)

    return precise_articles


# 3)
#
# Function: article_count
#
# Parameters:
#   count - max number of returned articles
#   titles - list of article titles to search through
#
# Returns: list of articles in given titles starting from the
# beginning that do not exceed given count in total. If there are no
# given article titles, return an empty list regardless of the count.
# If the max is larger than the # of titles, just return all titles.
def article_count(count, titles):
    # return 'count' number of articles from the list
    return titles[:count]


# 4)
#
# Function: random_article
#
# Parameters:
#   index - index at which article title to return
#   titles - list of article titles to search through
#
# Returns: article title in given titles at given index. If
# index is not valid, return an empty string
def random_article(index, titles):
    article = ''

    # assign article to the value at the index if within the range
    if index < len(titles):
        article = titles[index]

    # return the article
    return article


# 5)
#
# Function: favorite_article
#
# Parameters:
#   favorite - favorite article title
#   titles - list of article titles to search through
#
# Returns: True if favorite article is in the given articles
# (case insensitive) and False otherwise
def favorite_article(favorite, titles):
    # convert favourite word to lower case
    favorite_insesitive = favorite.lower()

    for article in titles:
        # chaeck if favourite word or phrase in teh article titles
        if favorite_insesitive in article.lower():
            return True

    # return False if the condition is never True
    return False


# 6)
#
# Function: multiple_keywords
#
# Parameters:
#   keyword - additional keyword to search
#   titles - article titles from basic search
#
# Returns: searches for article titles from entire list of available
# articles and adds those articles to list of article titles from basic
# search
def multiple_keywords(keyword, titles):
    new_articles = search(keyword)

    return titles + new_articles


# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-5)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article titles to contain only ones of the maximum length
        articles = title_length(value, articles)
    if advanced == 2:
        # value stores max number of articles
        # Update article titles to contain only the max number of articles
        articles = article_count(value, articles)
    elif advanced == 3:
        # value stores random number
        # Update articles to only contain the article title at index of the random number
        articles = random_article(value, articles)
    elif advanced == 4:
        # value stores article title
        # Store whether article title is in the search results into a variable named has_favorite
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
        # value stores keyword to search
        # Updated article titles to contain article titles from the first search and the second search
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")


if __name__ == "__main__":
    display_result()