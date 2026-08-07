from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from dotenv import load_dotenv
import os
load_dotenv()

DB_URL = os.getenv('URL')
print(DB_URL)

class AsyncDatabaseSesion:
    def __init__(self):
        self.engine = create_async_engine(
            DB_URL,
            echo=True,
            future=True,
        )

        self.session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def close(self):
        if self.engine is not None:
            await self.engine.dispose()

db = AsyncDatabaseSesion()

async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise