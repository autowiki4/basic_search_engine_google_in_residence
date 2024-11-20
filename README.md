# Basic Search Engine

A basic search engine that leverages article metadata to perform keyword-based and advanced searches, showcasing preprocessing and search functionalities for efficient data querying.

**Features**

**Keyword-based Search:** Searches through article titles and metadata to find relevant articles.

**Metadata Preprocessing:** Converts raw article data into dictionaries for optimized search operations.

**Advanced Search Options:** Filters results based on title length, author, keywords, publication year, and more.

**Data Structure**

Article metadata is stored as a 2D list, where each row represents an article with the following fields:

**Title (string)**: The title of the article.

**Author (string)**: The author's name.

**Timestamp (int)**: Unix time indicating when the article was published.

**Length (int)**: Number of characters in the article.

**Keywords (list of strings)**: Keywords related to the article's content.

# Future Enhancements
- Add support for stemming and case-insensitive searches.

- Introduce relevance ranking for better search result ordering.

- Implement real-time article fetching via APIs.
