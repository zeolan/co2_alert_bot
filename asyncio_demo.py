import asyncio

from app_logging import logger


async def periodic(interval: int):
    while True:
        logger.info('periodic %s', interval)
        await asyncio.sleep(interval)

# def stop():
#     task.cancel()

loop = asyncio.get_event_loop()
task1 = loop.create_task(periodic(6))
task2 = loop.create_task(periodic(3))
# loop.call_later(10, stop)

try:
    loop.run_until_complete(task1)
    loop.run_until_complete(task2)
except (asyncio.CancelledError, KeyboardInterrupt):
    task1.cancel()
    task2.cancel()
