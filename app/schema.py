from pydantic import BaseModel, Field
from typing import Optional, Literal

class PassengerInput(BaseModel):
    Pclass: int = Field(
        default=3,
        ge=1,
        le=3,
        example=3,
        description="Passenger class (1 = Upper, 3 = Lower)"
    )
    
    Name: str = Field(
        default="Braund, Mr. Owen Harris",
        min_length=3,
        example="Braund, Mr. Owen Harris",
        description="Full passenger name"
    )
    
    Sex: Literal["male", "female"] = Field(
        default="male",
        example="male",
        description="Gender of passenger"
    )
    
    Age: float = Field(
        default=30.0,
        ge=0,
        le=100,
        example=22,
        description="Age of passenger"
    )
    
    SibSp: int = Field(
        default=0,
        ge=0,
        le=10,
        example=1,
        description="Number of siblings/spouses aboard"
    )
    
    Parch: int = Field(
        default=0,
        ge=0,
        le=10,
        example=0,
        description="Number of parents/children aboard"
    )
    
    Fare: float = Field(
        default=32.0,
        ge=0,
        example=7.25,
        description="Ticket fare"
    )
    
    Embarked: Literal["C", "Q", "S"] = Field(
        default="S",
        example="S",
        description="Port of embarkation"
    )
    
    Cabin: Optional[str] = Field(
        default=None,
        example="C85",
        description="Cabin number (optional)"
    )