from pydantic import BaseModel

from pol.models import Subject


class Topic(BaseModel):
    subject: Subject


class TopicReply(BaseModel):
    topic: Topic
