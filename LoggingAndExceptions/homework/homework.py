import logging

logging.basicConfig(filename='test.log', filemode='w', level=logging.INFO, format='%(message)s')

class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:

    # add 2 class attributes - max_visitors (200) and min_visitors (10)
    max_visitors = 200
    min_visitors = 10

    def __init__(self, visitors_num):
        """
        if visitors num is bigger than max_visitors - raise TooManyVisitors error
        if visitors num is less than min_visitors - raise TooFewVisitors error
        """
        self.visitors_num = visitors_num
        self.count_visitors()


    def count_visitors(self):
        if self.visitors_num > self.max_visitors:
            raise TooManyVisitors
        if self.visitors_num < self.min_visitors:
            raise TooFewVisitors


def make_concert(visitors_num):
    """
    create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
    in case if caught - log error to console and return False, in case of successful initialization - return True
    """

    try:
        Concert(visitors_num)
        return True
    except (TooFewVisitors, TooManyVisitors):
        return False

# create Logger object
# set level to debug
# add handler to write logs to file "test.log"


def log_message(message, level):
    """
    this function should use the logger defined above and log messages.
    level is the numeric representation of log level the message should refer to.
    :param message:
    :param level:
    """
    if level == 30:
        logging.warning(message)
    else:
        logging.info(message)
