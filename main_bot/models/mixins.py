class BaseModelMixin:
    """Here's base queries for all models"""

    @classmethod
    async def get_all(cls) -> list:
        return await cls.query.gino.all()

    @classmethod
    async def reset_data(cls):
        await cls.delete.gino.status()
