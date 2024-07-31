import json
import webbrowser
import sys

# Change to true if you want to open the search in a new tab
new_tab = False


def load_config(config_file='idk_name.json'):
    with open(config_file, 'r') as file:
        return json.load(file)


def main(query):
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
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        main(query)
    else:
        print("Please provide a search query.")
