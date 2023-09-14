import re
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename=f'logreader.log',
                    filemode='w',
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    )


def main():
    result: dict = {}
    try:
        with open('events.log', 'r', encoding='utf-8') as logfile:
            pattern = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2}) \d{2}:(?P<minute>\d{2}):\d{2}')
            for line in logfile.readlines():
                if 'NOK' in line:
                    timestamp = pattern.search(line)[0][:-3]
                    result[timestamp] = result.get(timestamp, 0) + 1
    except FileNotFoundError as error:
        logging.exception(f'FileNotFoundError: {error.args}', exc_info=False)

    for timestamp, count in result.items():
        print(f'Timestamp: {timestamp}; NOK count: {count}')


if __name__ == '__main__':
    main()
