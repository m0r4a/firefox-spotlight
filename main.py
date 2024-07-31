import json
import webbrowser
import sys

# Change to true if you want to open the search in a new tab
new_tab = False


def load_config():
    try:
        with open("local_shortcuts.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        sys.exit(
            "No config file found. Please create a local_shortcuts.json file."
        )


def main():
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    else:
        sys.exit("Please provide a search query.")

    config = load_config()
    shortcuts = config.get('shortcuts', {})
    search_engines = config.get('search_engines', {})
    default_search_engine = config.get(
        'default_search_engine', 'https://duckduckgo.com/?q=')

    if query in shortcuts:
        url = shortcuts[query]
    else:
        engine_key = query.split()[0]
        search_term = ' '.join(query.split()[1:])
        if engine_key in search_engines:
            url = search_engines[engine_key] + search_term
        else:
            url = default_search_engine + query

    if new_tab:
        webbrowser.get('firefox').open_new_tab(url)
    else:
        webbrowser.get('firefox').open_new(url)


if __name__ == '__main__':
    main()
