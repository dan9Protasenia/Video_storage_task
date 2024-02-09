FROM python:3.12-slim as base
ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100
ENV \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
# Final path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl gcc python3-dev \
    && curl -sSL https://install.python-poetry.org | python - --version 1.6.1 \
    && apt-get remove -y curl \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $PYSETUP_PATH

COPY poetry.lock pyproject.toml ./

RUN poetry install --with dev,app

FROM base as final

COPY --from=base $PYSETUP_PATH $PYSETUP_PATH

WORKDIR /project

COPY src ./src

EXPOSE 8000

CMD ["uvicorn", "src.app.main:app", "--host", "127.0.0.1", "--port", "8000/docs"]