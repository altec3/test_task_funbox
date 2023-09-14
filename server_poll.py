import asyncio
from datetime import datetime
from pydantic import BaseModel
import aiohttp
import logging

SERVERS = ['maria.ru', 'rose.ru', 'sina.ru']

logging.basicConfig(level=logging.DEBUG,
                    filename=f'server_poll.log',
                    filemode='w',
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    )


class Response(BaseModel):
    """ Производит валидацию ответа от сервера. """

    count: int


async def get_metric(session: aiohttp.ClientSession, server: str) -> tuple:
    """ Получает метрики с сервера. """

    try:
        async with session.get(f'http://{server}/api/count') as response:
            logging.debug(f'{response.url}')
            count: int = Response(**await response.json()).count
            return server, count
    except aiohttp.ContentTypeError as error:
        logging.exception(f'[get_metric] ContentTypeError: {error.message}', exc_info=False)
        return server, 'Poll error. See "server_poll.log"'


def print_result(server: str, metric: int) -> None:
    """ Выводит в консоль результаты опроса. """

    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {server} {metric}')


async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [asyncio.create_task(get_metric(session, server)) for server in SERVERS]
            results: tuple[tuple] = await asyncio.gather(*tasks)
            for result in results:
                print_result(*result)

            await asyncio.sleep(60)


if __name__ == '__main__':
    asyncio.run(main())
