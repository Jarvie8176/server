import datetime
from typing import Optional

from pydantic import Field, BaseModel

from pol.models import Subject


class Topic(BaseModel):
    subject: Subject
    pass


class TopicReply(BaseModel):
    topic: Topic
