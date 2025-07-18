from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, BigInteger, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(unique=True)
    age:Mapped[int] = mapped_column()
    city:Mapped[str] = mapped_column()


class Message(Base):
    __tablename__ = "messages"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message:Mapped[str] = mapped_column(String(50))
    description:Mapped[str] = mapped_column(String(100))