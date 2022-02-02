from apicalls import *
import asyncio
import os
import random
import logging

os.environ["AUTOWRAPT_BOOTSTRAP"] = "autodynatrace"
wait_number = random.uniform(0, 4)
logging.basicConfig(level = logging.INFO, filename = 'apicalls.log')

logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

async def getcall():
    while True:
        await asyncio.sleep(wait_number)
        getpayload()


async def postcall():
    while True:
        await asyncio.sleep(wait_number)
        postpayload()


"""async def publicall():
    while True:
        await asyncio.sleep(1.9)
        getpublic()


async def externalcall():
    while True:
        await asyncio.sleep(43.1)
        getexternal()

cors_loop = asyncio.wait([getcall(), postcall(), publicall(), externalcall()])"""


loop = asyncio.get_event_loop()
cors_loop = asyncio.wait([getcall(), postcall()])
loop.run_until_complete(cors_loop)
