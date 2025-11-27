# Fullstack web application template

Fullstack web-app template for easy project scaffolding.

Tech stack:

- frontend: React, TypeScript, TailwindCSS, Vite
- backend: Python, FastAPI

## How to use

### Prerequisites

- [Node.js](https://nodejs.org/en)
- [bun](https://bun.com)
- [Python](https://python.org) (>=3.14 required)

If you have Node.js, installed on your machine, run `npm install -g bun` to install bun globally.

### Frontend

1. Navigate to frontend
2. Run these commands

```
bun install
bun dev
```

### Backend

1. Navigate to backend
2. Add following config to `.env` file:

```env
PROJECT_ENV=development
```

3. Run these commands:

```
python -m venv .venv
./.venv/Scripts/activate
pip install poetry
poetry install

python ./src/main.py
```
