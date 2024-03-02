from fastapi import FastAPI

app = FastAPI()

@app.get("/lowercase/{word}")
async def conv_lowercase(word:str):

    lowercase_word = word.lower()

    return {"original_word": word, "lowercase_word": lowercase_word}

