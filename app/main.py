from fastapi import FastAPI
from app.routers import main, tracks, author


app = FastAPI(title='Music Api')
app.include_router(main.router)
app.include_router(tracks.router)
app.include_router(author.router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8080, host='127.0.0.1')
