import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola</h1>
        <p>Mundo</p>
"""

def run():
    store.getCategories()

if __name__ == '__main__':
    run()