from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app=FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Магазин питонов</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>🐍 Добро пожаловать в магазин королевских питонов!</h1>
        <p>Здесь вы найдете самых красивых и здоровых питомцев.</p>
        <a href="/pythons">
            <button>📋 Посмотреть список питонов</button>
        </a>

        <a href='/shop'>
            <button>магазинчик</button>
        </a>
        

        <a href="https://t.me/ptnbll" target="_blank">
            <button>💬 Связаться в Telegram</button>
        </a>
    </body>
    </html>
    """
    return html_content

@app.get('/pythons')
def get_pythons():
    return {
        'pythons':[
        {'name': 'Mojave', 'price': 16000, 'sex':'male'},
        {'name': 'Lesser', 'price': 18000, 'sex':'female'},
        {'name': 'BEL', 'price': 30000, 'sex':'male'},
        {'name': 'Black pastel', 'price': 20000, 'sex':'male'}
    ]
    }

@app.get("/shop")
def shop():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Выбор питонов</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Выводок 27-го года</h1>
        <ul>
            <li><strong>Mojave</strong> — 16 000 ₽ (самец)</li>
            <li><strong>Lesser</strong> — 18 000 ₽ (самка)</li>
            <li><strong>BEL</strong> — 30 000 ₽ (самец)</li>
            <li><strong>Black pastel</strong> - 20000 ₽ (самец)</li>
        </ul>
        <p> 

            <a href="/">
                <button>перейти на главную страницу</button>
            </a>

            <a href="https://t.me/ptnbll" target="_blank">
                <button> узнать подробности в Telegram</button>
            </a>
        </p>
    </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)