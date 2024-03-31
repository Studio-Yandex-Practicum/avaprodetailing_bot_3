from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.core.config import settings


class User(Base):
    tg_id = Column(Integer, nullable=True)
    surname = Column(
        String(settings.max_fio_len), comment='Фамилия', nullable=False)
    name = Column(
        String(settings.max_fio_len), comment='Имя', nullable=False)
    patronymic = Column(
        String(settings.max_fio_len), comment='Отчество', nullable=True)
    date_birth = Column(Date, comment='Дата рождения', nullable=False)
    phone = Column(String, unique=True, nullable=False)
    reg_date = Column(DateTime, default=datetime.now)
    role = Column(
        Integer, ForeignKey('role.id'), default=settings.default_role)
    reservations = relationship('Car', cascade='delete')
