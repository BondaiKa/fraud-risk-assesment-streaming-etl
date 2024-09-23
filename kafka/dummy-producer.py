from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import json
import os
import logging
import asyncio
import sys

log = logging.getLogger(__name__)

async def run(connection_string: str, eventhub_name:str):
    """Let's create dummy producer that sends example of transations to  Kafka/ Azure Event hub """
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str=connection_string, 
            eventhub_name=eventhub_name,
        )
    except Exception as e:
        log.error(f"Unexpected error while creating EventHubProducerClient. Message error:'{e}'")
        log.debug(f"connection_string {connection_string}; eventhub_name {eventhub_name}")
        sys.exit(1)

    async with producer:
        log.debug(f"Start to create batch...")

        event_data_batch = await producer.create_batch()

        with open("/Users/ksafiullin/src/data-engineer-case-study/data/transaction-high-risk.json") as f:
            example_of_high_risk_transaction = json.load(f)

        with open("/Users/ksafiullin/src/data-engineer-case-study/data/transaction-low-risk.json") as f:
            example_of_low_risk_transaction = json.load(f)

        event_data_batch.add(EventData(json.dumps(example_of_high_risk_transaction)))
        event_data_batch.add(EventData(json.dumps(example_of_low_risk_transaction)))

        log.debug(f"event_data_batch dict {event_data_batch.__dict__}")

        await producer.send_batch(event_data_batch)

    log.debug(f"Finish sending events...")

if __name__ == "__main__":
    logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO)

    EVENT_HUB_CONNECTION_STR = os.environ.get("AZURE_APPCONFIG_CONNECTION_STRING")
    EVENT_HUB_NAME = os.environ.get("AZURE_APPCONFIG_EVENT_HUB_NAME")

    if not EVENT_HUB_CONNECTION_STR:
        raise ValueError(
            "AZURE_APPCONFIG_CONNECTION_STRING wasn't configured."
            "Be sure that you have in your environment")
    
    if not EVENT_HUB_NAME:
        raise ValueError(
            "AZURE_APPCONFIG_EVENT_HUB_NAME wasn't configured."
            "Be sure that you have in your environment")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        run(
            connection_string=EVENT_HUB_CONNECTION_STR,
            eventhub_name=EVENT_HUB_NAME,
        )
    )
