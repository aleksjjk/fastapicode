from sqlalchemy import select

from database import new_session, TaskOrm
from scemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()  # work with dictionary
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()  # send to database but yet not save it
            await session.commit()  # save all and commit changes
            return task.id

    @classmethod
    async def find_all(cls)->list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_scemas = [STask.model_validate(task_model)
                            for task_model in task_models]
            return task_scemas
