from connect import connect
from models import Author, Quote


def search_quotes(query):
    print(f"Executing query: {query}")

    if query.startswith("name"):
        author_name = query.split(":")[1].strip()
        print(f"Author name to search: {author_name}")
        author = Author.objects(fullname__icontains=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            return quotes
        else:
            return []

    elif query.startswith("tags:"):
        tags = [t.strip() for t in query.split(":")[1].split(",")]
        print(f"Tags to search: {tags}")
        quotes = Quote.objects(tags__in=tags)
        return quotes

    elif query.startswith("tag"):
        tag = query.split(":")[1].strip()
        print(f"Tag to search: {tag}")
        quotes = Quote.objects(tags__icontains=tag)
        return quotes

    else:
        return []


if __name__ == "__main__":
    while True:
        user_input = input("Enter the command: ")
        if user_input.lower() == "exit":
            break

        quotes_result = search_quotes(user_input)
        print(f"Number of quotes found: {len(quotes_result)}")
        for quote in quotes_result:
            author_name = quote.author.fullname
            quote_text = quote.quote
            print(f"Author: {author_name}, Quote: {quote_text}")