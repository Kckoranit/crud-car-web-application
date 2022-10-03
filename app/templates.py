from fastapi import Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

import typing

class Templates(Jinja2Templates):
    
    def __init__(self, directory: str, **env_options: typing.Any) -> None:
        super().__init__(directory, **env_options)
        
    def redirect_to(self, url: str):
        return RedirectResponse(url, status_code=status.HTTP_302_FOUND)
    
    def go_to(self, html: str, request: Request, title: str, data: dict = {}, status_code: int = status.HTTP_200_OK):
        context = {
            'request': request,
            'title': title,
            **data
        }
        response = self.TemplateResponse(html, context, status_code=status_code)
        return response
    
templates = Templates(directory='templates')