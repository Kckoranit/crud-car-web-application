from fastapi import APIRouter, Request, status, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from .crud import crud
from .dependencies import get_create_car_form, get_update_car_form
from .schema import Car
from .templates import templates

router = APIRouter()

@router.get('/', response_class=RedirectResponse)
def get_root():
    return templates.redirect_to('/cars')

@router.get('/cars', response_class=HTMLResponse)
def get_index_page(request: Request):
    cars = crud.read_all_cars()
    if cars:
       data = {
           'cars': cars,
       }
       return templates.go_to('index.html', request, 'car-app', data)
    return templates.go_to('empty-database.html', request, 'empty-database', status_code=status.HTTP_404_NOT_FOUND)

################################################################################################################################################

@router.get('/create', response_class=HTMLResponse)
def get_create_car_page(request: Request):
    data = {
        'countries': crud.read_all_countries()
    }
    return templates.go_to('create-car.html', request, 'create-car', data)

@router.post('/cars', response_class=RedirectResponse)
def create_car(car: Car = Depends(get_create_car_form)):
    crud.create(car)
    return templates.redirect_to('/cars') 

################################################################################################################################################


@router.post('/cars/{id}', response_class=RedirectResponse)
def update_car(id: int, car: Car = Depends(get_update_car_form)):
    crud.update(id, car)
    return templates.redirect_to('/cars')

@router.get('/edit', response_class=HTMLResponse)
def get_edit_car_page(request: Request, id: int):
    data = {
        'id': id,
        'car': crud.read_car_by_id(id),
        'countries': crud.read_all_countries()
    }
    return templates.go_to('edit-car.html', request, 'edit-car', data)

################################################################################################################################################


@router.get('/cars/{id}', response_class=HTMLResponse)
def get_search_page(request: Request, id: int):
    car = crud.read_car_by_id(id)
    if car:
        data = {
            'car': car,
            'id': id
        }
        return templates.go_to('search-car.html', request, 'search-car', data)
    return templates.go_to('not-found.html', request, 'not-found-car', status_code=status.HTTP_404_NOT_FOUND)

@router.post('/search', response_class=RedirectResponse)
def search_car(id: int = Form(...)):
    return templates.redirect_to(f'/cars/{id}')

################################################################################################################################################

@router.get('/delete/{id}', response_class=RedirectResponse)
def delete_car(id: int):
    crud.delete(id)
    return templates.redirect_to('/cars')


 



