# Web Search Tool
import webbrowser

def search_web(query):
    """
    Search the web using the default browser.
    """
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Opened browser to search for: {query}"
