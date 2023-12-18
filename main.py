from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastui import prebuilt_html

from google.home import router as home_router


app = FastAPI()
app.include_router(home_router)


@app.get('/{path:path}')
def error_404() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='404'))


def run_app() -> None:
    import uvicorn

    uvicorn.run('main:app', reload=True)


if __name__ == '__main__':
    run_app()
