from fastapi import APIRouter

from app.main import nlp, Message

router = APIRouter()


@router.get("/")
async def root():
    return "Test router"


@router.post("/generative/")
async def generate(message: Message):
    message.output = nlp.generate(prompt=message.input)
    return {"output": message.output}


@router.post("/sentiment/")
async def sentiment_analysis(message: Message):
    message.output = str(nlp.sentiments(message.input))
    return {"output": message.output}
