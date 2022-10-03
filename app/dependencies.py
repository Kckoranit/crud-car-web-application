
from fastapi import Form
from typing import Optional, List
from .schema import Car

def get_create_car_form(
    make: str = Form(...),
    model: str = Form(...),
    year: Optional[int] = Form(1950, ge=1900, le=2022),
    price: Optional[float] = Form(0, ge=0),
    engine: Optional[str] = Form(...),
    autonomus: Optional[bool] = Form(True),
    sold: List[Optional[str]] = Form([]),
):
    return Car(
        make=make,
        model=model,
        year=year,
        price=price,
        engine=engine,
        autonomus=autonomus,
        sold=sold
    )
    
def get_update_car_form(
    make: Optional[str] = Form(None),
    model: Optional[str] = Form(None),
    year: Optional[int] = Form(None),
    price: Optional[float] = Form(None),
    engine: Optional[str] = Form(None),
    autonomus: Optional[bool] = Form(None),
    sold: List[Optional[str]] = Form([]),
):
    return Car(
        make=make,
        model=model,
        year=year,
        price=price,
        engine=engine,
        autonomus=autonomus,
        sold=sold
    )