from typing import List

from fastapi import FastAPI

from bewise.app.crud import create_new_application, get_all_applications
from bewise.app.schemas import ApplicationCreate, ApplicationDB
import uvicorn

from bewise.logger.logger import logger

app = FastAPI()


@app.post('/applications', response_model=ApplicationDB)
async def create_application(application: ApplicationCreate):
    new_application = await create_new_application(application)
    return new_application


@app.get('/applications', response_model=List[ApplicationDB])
async def get_applications():
    applications = await get_all_applications()
    return applications

if __name__ == '__main__':
    try:
        uvicorn.run('main:app', reload=True)
    except Exception as err:
        logger.error(err, exc_info=True)
