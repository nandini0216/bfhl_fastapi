from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from typing import List, Any, Dict, Optional
import os

app = FastAPI(title="BFHL API", version="1.0.0")

# ---- Configuration (edit these for your own submission) ----
FULL_NAME_LOWER = os.getenv("FULL_NAME_LOWER", "john_doe")  # e.g., "rishita_nigam"
DOB_DDMMYYYY = os.getenv("DOB_DDMMYYYY", "17091999")        # e.g., "14062003"
EMAIL = os.getenv("EMAIL", "john@xyz.com")
ROLL_NUMBER = os.getenv("ROLL_NUMBER", "ABCD123")

USER_ID = f"{FULL_NAME_LOWER}_{DOB_DDMMYYYY}"

class Payload(BaseModel):
    data: List[str] = Field(..., description="Array of strings to process")

def is_numeric_str(s: str) -> bool:
    # strictly digits only (no signs/decimal points) as per examples
    return s.isdigit()

def is_alpha_str(s: str) -> bool:
    return s.isalpha()

def alternating_caps_reverse(letters: List[str]) -> str:
    # letters: list of single alphabetic characters in original order
    rev = list(reversed(letters))
    out_chars = []
    for i, ch in enumerate(rev):
        if i % 2 == 0:
            out_chars.append(ch.upper())
        else:
            out_chars.append(ch.lower())
    return "".join(out_chars)

@app.post("/bfhl")
async def bfhl(payload: Payload):
    try:
        items = payload.data

        odd_numbers: List[str] = []
        even_numbers: List[str] = []
        alphabets: List[str] = []
        special_characters: List[str] = []
        total_sum = 0

        # Gather characters for alternating caps string (all alphabetic chars from entire input)
        alpha_chars_in_order: List[str] = []

        for token in items:
            if is_numeric_str(token):
                # keep original token as string
                n = int(token)
                total_sum += n
                if n % 2 == 0:
                    even_numbers.append(token)
                else:
                    odd_numbers.append(token)
            elif is_alpha_str(token):
                alphabets.append(token.upper())
                # collect each alphabetic character
                for ch in token:
                    if ch.isalpha():
                        alpha_chars_in_order.append(ch)
            else:
                # special token (contains non-alnum or mix like "a1", "#", etc.)
                special_characters.append(token)
                # still collect alphabetic characters from mixed tokens
                for ch in token:
                    if ch.isalpha():
                        alpha_chars_in_order.append(ch)

        concat_string = alternating_caps_reverse(alpha_chars_in_order)
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string,
        }
        return response
    except Exception:
        # As per prompt, always return status in body; keep HTTP 200 with is_success=false
        return {
            "is_success": False,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": [],
            "even_numbers": [],
            "alphabets": [],
            "special_characters": [],
            "sum": "0",
            "concat_string": ""
        }
