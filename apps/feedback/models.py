from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from virgo.core.database import Base
from virgo.core.mixins import BaseModelMixin


class Feedback(Base, BaseModelMixin):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    feedback_type = Column(String(50), nullable=False)
    message = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)