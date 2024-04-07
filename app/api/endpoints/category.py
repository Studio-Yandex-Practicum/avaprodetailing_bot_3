from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_fields_duplicate, check_exist
from app.core.db import get_async_session
from app.crud.category import category_crud
from app.models import Category
from app.schemas.category import CategoryDB, CategoryCreate, CategoryUpdate

router = APIRouter()


@router.post(
    '/',
    response_model=CategoryDB,
    response_model_exclude_none=True,
    # dependencies=[Depends(current_superuser)],
)
async def create_new_category(
    new_category_json: CategoryCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Category:
    """
    Создание категории услуг.
    Только для суперюзеров.
    """
    # Словарь с данными, которые нужно проверить на уникальность.
    fields_for_check = {
        'name': new_category_json.name,
    }
    # Проверка на уникальность всех данных
    await check_fields_duplicate(category_crud, fields_for_check, session)
    # Создание категории услуг
    new_category_db = await category_crud.create(new_category_json, session)
    return new_category_db


@router.get(
    '/',
    response_model=list[CategoryDB],
    response_model_exclude_none=True,
)
async def get_all_categories(
    session: AsyncSession = Depends(get_async_session),
):
    """Возвращает список всех категорий услуг."""
    return await category_crud.get_multi(session)


@router.patch(
    '/{category_id}',
    response_model=CategoryDB,
    # dependencies=[Depends(current_superuser)],
)
async def update_category(
    category_id: int,
    category_json: CategoryUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Редактирование категории.
    """

    # Проверка на существование категории в базе
    category_db = await check_exist(category_crud, category_id, session)

    # Проверка на уникальность переданных данных
    if category_json.name is not None:
        fields_for_check = {'name': category_json.name, }
        await check_fields_duplicate(category_crud, fields_for_check, session)

    # Изменяем поля категории
    return await category_crud.update(category_db, category_json, session)


@router.delete(
    '/{category_id}',
    response_model=CategoryDB,
    # dependencies=[Depends(current_superuser)],
)
async def delete_category(
    category_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Удаляет категорию.
    """
    # Проверка на существование категории в базе
    category_db = await check_exist(category_crud, category_id, session)

    # Удаляем категорию.
    point_db = await category_crud.remove(category_db, session)
    return point_db