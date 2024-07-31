# Firefox spotlight

## Why?

It is very common for me to open Firefox directly to perform a search. Unlike Steam or Netflix, which I might open and then decide what to look for, with Firefox, usually you have a specific search in mind.

I don't like the process of opening Firefox with a command and then, once it's open, performing the search I intended. This might seem like a small detail, but I believe that the combination of small details adds up to make a better or worse experience when using a computer, working, or doing anything else.

## Firefox can be used from the command line

While you can use any of these commands:

- `firefox <url>`
- `firefox --new-window <url>`
- `firefox --new-tab <url>`
- `firefox --search <term>`

And indeed, you open Firefox, but none of these (as far as I know) support the use of shortcuts for bookmarks. Additionally, if you use different search engines besides your default one, you can't switch them because, even though the `--search` flag is meant to search for things, it only does so with your default search engine.

## Objective

The goal of this project is to create an application similar to macOS Spotlight, but its sole function will be to perform searches in Firefox.
