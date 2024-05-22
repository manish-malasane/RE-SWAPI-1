import logging

logging.basicConfig(
    filename="utility/tracker.log", encoding="utf-8", level=logging.INFO
)


def mylogger(func):
    def wrapper(url):
        try:
            logging.info(f"We are hitting this url - {url}")
            result = func(url)
            logging.info(f" status code:- {result.status_code}")
            return result
        except Exception:
            logging.error(f"There are some issues while fetching the code")

    return wrapper

