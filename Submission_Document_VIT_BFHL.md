
# Submission Document – BFHL API (/bfhl)

**Name:** <Your Full Name>  
**User ID (format: full_name_ddmmyyyy):** `<full_name_ddmmyyyy>`  
**Email:** <your_email@vit.ac.in>  
**College Roll Number:** <Your Roll No.>  

**Hosted Endpoint (POST):** `https://<your-app>.onrender.com/bfhl`  
**Status code on success:** 200

## Tech Stack
- Language: Python
- Framework: FastAPI
- Hosting: Render (alternative: Railway)

## How to Test (sample)
**Request Body**
```json
{ "data": ["a","1","334","4","R","$"] }
```
**Response (example)**
```json
{
  "is_success": true,
  "user_id": "<full_name_ddmmyyyy>",
  "email": "<your_email@vit.ac.in>",
  "roll_number": "<Your Roll No.>",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Notes
- Numbers are returned as strings.
- `alphabets` contains only alphabet-only tokens, uppercased.
- `special_characters` contains tokens that are neither strictly alphabetic nor strictly numeric.
- `concat_string` is built from all alphabetic **characters** found in input (including inside mixed tokens), then reversed and rendered in alternating caps.
