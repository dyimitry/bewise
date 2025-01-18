import json
from aiokafka import AIOKafkaProducer
from bewise.app.config import settings
import asyncio


async def get_kafka_producer():
    producer = AIOKafkaProducer(
        loop=asyncio.get_event_loop(),
        bootstrap_servers=settings.kafka_broker
    )
    await producer.start()
    return producer


async def publish_to_kafka(producer: AIOKafkaProducer, data: dict):
    try:
        message = json.dumps(data).encode('utf-8')
        await producer.send_and_wait(settings.kafka_topic, message)
    except Exception as err:
        print(f"Error publishing to Kafka: {err}")
    finally:
        await producer.stop()
