from typing import List, Optional

from beanie import Document
from pydantic import Field


class Institution(Document):
    name: str = Field(
        ..., description="Unique institution name, normalized (e.g. 'enem')"
    )
    display_name: str = Field(..., description='Full name of the institution')
    country: str = Field(default='BR', description='Country code')

    class Settings:
        name = "institutions"


class Exam(Document):
    title: str = Field(..., description="Exam title (e.g. 'ENEM 2023')")
    institution: str = Field(..., description='Institution name reference')
    year: int = Field(..., description='Year of the exam')
    disciplines: List[str] = Field(..., description='List of subject areas')

    class Settings:
        name = "exams"


class Question(Document):
    title: str = Field(..., description='Unique question identifier')
    institution: str = Field(..., description='Institution name')
    exam_title: str = Field(
        ..., description="Title of the exam (e.g. 'ENEM 2023')"
    )
    year: int = Field(..., description='Year of the exam')
    index: int = Field(..., description='Position in exam')
    area: str = Field(..., description='Subject area')
    language: Optional[str] = Field(
        None, description='Language of the question'
    )
    question_text: Optional[str] = Field(
        None, description='Question statement'
    )
    files: Optional[str] = Field(None, description='Path to associated file')
    alternative_introduction: Optional[str] = Field(
        None, description='Intro to alternatives'
    )
    correct_answer: str = Field(..., description='Correct answer key')
    alternatives: List[str] = Field(..., description='Answer choices')

    class Settings:
        name = "questions"
