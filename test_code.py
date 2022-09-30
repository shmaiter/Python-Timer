from reader import feed
from timer import Timer


if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'

    t = Timer(text="Downloaded 10 tutorials in {:0.2f} seconds")
    t.start()
    for tutorial_num in range(10):
        tutorial = feed.get_titles(tutorial_num)
        print(tutorial)
    t.stop()
