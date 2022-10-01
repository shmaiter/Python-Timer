from reader import feed
from timer import Timer


def main():
    # t = Timer(text="Downloaded 10 tutorials in {:0.2f} seconds")
    # if constructor inside variables aren't defined it will assing it to the first it encounters inside the class.
    t = Timer('download', logger=None)
    for num in range(10):
        t.start()
        tutorial = feed.get_article(num)
        t.stop()
        print(tutorial)

    download_time = Timer.timers['download']
    print(f'Downloaded 10 tutorials in {download_time:.4f} seconds')


if __name__ == '__main__':
    main()
