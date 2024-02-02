import multipart
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
from fastapi.templating import Jinja2Templates


# Create the FastAPI instance
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_root_html(request: Request) -> HTMLResponse:
    """
    Hmmm, what does this do? What is a template response? How can it help us?
    Renders the index.html template, with the request object passed in.
    :param request:
    :return:
    """
    return templates.TemplateResponse('index.html', {'request': request})


@app.get("/basics", response_class=HTMLResponse)
def get_basics_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('basics.html', {'request': request})


@app.get("/css", response_class=HTMLResponse)
def get_css_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('css.html', {'request': request})


@app.get("/fast_api", response_class=HTMLResponse)
def get_fast_api_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('fast_api.html', {'request': request})


@app.get("/view_notes", response_class=HTMLResponse)
def get_view_notes_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('notes.html', {'request': request})


@app.get("/web_development", response_class=HTMLResponse)
def get_web_development_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('web_development.html', {'request': request})

@app.get("/web_serving", response_class=HTMLResponse)
def get_web_serving_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('web_serving.html', {'request': request})





@app.get("/notes")
async def read_notes():
    """
    Read the notes from the file and return them.
    :return:
    """
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No notes yet."
    return {"notes": content}


@app.post("/notes")
async def write_notes(note: str = Form(...)):
    """
    Write the notes to the file. post your messages to the notes endpoint.
    :param note:
    :return:
    """
    with open("notes.txt", "w") as file:
        file.write(note)
    return {"message": "Note saved successfully."}


# an example of a path parameter
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/slowdemo")
async def get_demo():
    with open("templates/slowdemo.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/slowroute")
async def slow_route():
    await asyncio.sleep(3)  # Artificial delay
    return {"message": "Delayed response received"}

@app.get("/timezones")
async def get_timezone():
    await asyncio.sleep(1);
    return {"timezone": ['CST', 'PST']}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
