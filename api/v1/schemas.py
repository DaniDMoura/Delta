from typing import List, Optional

from pydantic import BaseModel


class Institution(BaseModel):
    name: str
    display_name: str
    country: str


class ListInstitutions(BaseModel):
    Institutions: List[Institution]


class Exam(BaseModel):
    title: str
    institution: str
    year: int
    disciplines: List[str]


class ListExam(BaseModel):
    Exams: List[Exam]


class Question(BaseModel):
    title: str
    institution: str
    exam_title: str
    year: int
    index: int
    area: str
    language: Optional[str]
    question_text: Optional[str]
    files: Optional[str]
    alternative_introduction: Optional[str]
    correct_answer: str
    alternatives: List[str]


class ListQuestion(BaseModel):
    Questions: List[Question]
