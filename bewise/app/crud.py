from sqlalchemy import select

from bewise.app.models import Application, AsyncSessionLocal
from bewise.app.producer import get_kafka_producer, publish_to_kafka
from bewise.app.schemas import ApplicationCreate, ApplicationDB
from typing import List


async def create_new_application(
        new_application: ApplicationCreate
) -> Application:
    new_application = new_application.dict()

    db_application = Application(user_name=new_application['user_name'], description=new_application['description'])

    async with AsyncSessionLocal() as session:
        session.add(db_application)

        await session.commit()

        await session.refresh(db_application)

        application_data = {
            "id": db_application.id,
            "user_name": db_application.user_name,
            "description": db_application.description,
            "created_at": db_application.created_at.isoformat()  # Преобразование datetime в строку
        }
        producer = await get_kafka_producer()
        await publish_to_kafka(producer, application_data)

    return db_application


async def get_all_applications() -> List[ApplicationDB]:
    list_of_applications = []
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Application))
        applications = result.scalars().all()

        for model in applications:
            application: ApplicationDB = ApplicationDB(
                id=model.id,
                user_name=model.user_name,
                description=model.description,
                created_at=model.created_at,
            )
            list_of_applications.append(application)

    return applications
