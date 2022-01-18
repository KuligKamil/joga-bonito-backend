from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/')
async def home():
    return {'headers': [
        {'text': 'Player 1', 'value': 'player1'},
        {'text': 'Result', 'value': 'result'},
        {'text': 'Player 2', 'value': 'player2'},
        {'text': 'Is Done', 'value': 'isDone'},
        {'text': 'Details', 'value': 'data'},
    ],
        'games': [{
            'player1': {
                'id': '197038da-a28f-47a8-aa78-ecc721315c0f',
                'ranking': 2847,
                'name': 'Magnus Carlsen'
            }, 'player2': {
                'id': '08933fe1-bcb8-4669-8f44-faaecaaa1645',
                'ranking': 1800,
                'name': 'Andrea Botez'
            },
            'result': '0:1',
            'date': '1 quarter 2022',
        }, {
            'player1': {
                'id': '197038da-a28f-47a8-aa78-ecc721315c0f',
                'ranking': 1999,
                'name': 'John Rambo'
            }, 'player2': {
                'id': '08933fe1-bcb8-4669-8f44-faaecaaa1645',
                'ranking': 2000,
                'name': 'Rocky Balboa'
            },
            'result': '1:1',
            'date': '4 quarter 2022',
        }]
    }
