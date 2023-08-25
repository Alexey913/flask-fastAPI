# API должно поддерживать следующие операции:
# ○ Получение списка всех пользователей: GET /users/
# ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
# ○ Создание нового пользователя: POST /users/
# ○ Обновление информации о пользователе: PUT /users/{user_id}/
# ○ Удаление пользователя: DELETE /users/{user_id}/

# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    username: str = Field(title='Имя пользователя',min_length=2, max_length=30)
    email: str = Field(title='E-mail')
    password: str = Field(title = "Пароль", min_length=6)


class User(BaseModel):
    id: int = Field(title="id")
    username: str = Field(title='Имя пользователя',min_length=2, max_length=30)
    email: str = Field(title='E-mail')
    password: str = Field(title = "Пароль", min_length=6)

class PostIn(BaseModel):
    user_id: int
    post: str

class Post(BaseModel):
    id: int
    user: User
    post: str