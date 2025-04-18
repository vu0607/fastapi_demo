from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


movie_images = {
    "action": "https://tiki.vn/blog/wp-content/uploads/2023/12/phim-hanh-dong-extraction-1-692x1024.jpg",
    "romance": "https://m.yodycdn.com/blog/phim-tinh-cam-au-my.jpg",
}

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get_image/{genre}")
def get_image(genre: str):
    image_url = movie_images.get(genre.lower())
    if image_url:
        return {"imageUrl": image_url}
    else:
        return JSONResponse(
            status_code=404,
            content={"message": "Genre not found"}
        )


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8989,
        host="0.0.0.0",
        log_level="info",
    )
