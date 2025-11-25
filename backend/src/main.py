import uvicorn

from constants import APP_HOST, APP_PORT, DEVELOPMENT_ENV, PROJECT_ENV


def main() -> None:
    is_development_env = PROJECT_ENV == DEVELOPMENT_ENV
    uvicorn.run(
        app="root:app",
        host=APP_HOST,
        port=APP_PORT,
        reload=is_development_env,
    )


if __name__ == "__main__":
    main()
