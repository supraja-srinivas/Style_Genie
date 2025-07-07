from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from utils.image_analysis import detect_skin_tone_from_image

app = FastAPI()

class UserInput(BaseModel):
    text: str
    gender: str  # "male", "female", "other"

@app.post("/analyze-text")
def analyze_text(data: UserInput):
    text = data.text.lower()
    gender = data.gender.lower()

    if "fair" in text:
        tone = "Fair"
    elif "medium" in text:
        tone = "Medium"
    elif "dark" in text:
        tone = "Dark"
    else:
        tone = "Medium"

    recommendations = {
        "Fair": {
            "colors": ["Lavender", "Emerald", "Blush"],
            "ethnic": ["Pastel saree", "Ivory kurti"],
            "western": ["Soft tops", "Navy jeans"]
        },
        "Medium": {
            "colors": ["Coral", "Olive", "Mustard"],
            "ethnic": ["Printed gown", "Green salwar"],
            "western": ["Teal one-piece", "Maroon crop top"]
        },
        "Dark": {
            "colors": ["Cobalt Blue", "White", "Rust"],
            "ethnic": ["Royal blue saree", "Orange kurti"],
            "western": ["Bold prints", "White shirt"]
        }
    }

    return {
        "skin_tone": tone,
        "recommended_colors": recommendations[tone]["colors"],
        "ethnic": recommendations[tone]["ethnic"],
        "western": recommendations[tone]["western"]
    }

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    skin_tone = detect_skin_tone_from_image(image_bytes)
    return {"skin_tone": skin_tone}
 
