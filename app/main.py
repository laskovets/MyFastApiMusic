from fastapi import FastAPI
from routers import main, tracks, author, authentication


app = FastAPI(title='Music Api')
app.include_router(main.router)
app.include_router(tracks.router)
app.include_router(author.router)
app.include_router(authentication.router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8080, host='0.0.0.0')
