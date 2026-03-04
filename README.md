# hello-world

Simple FastAPI calculator API.

## Setup

- Create and activate a virtualenv (optional but recommended).
- Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` in your browser to try the interactive Swagger UI.

## Example request

`POST /calculate` with JSON body:

```json
{
  "a": 5,
  "b": 2,
  "op": "/"
}
```

Response:

```json
{
  "a": 5.0,
  "b": 2.0,
  "op": "/",
  "result": 2.5
}
```

Supported operations are `"+"`, `"-"`, `"*"`, and `"/"`.

## Tests

Run unit tests with:

```bash
pytest
```
