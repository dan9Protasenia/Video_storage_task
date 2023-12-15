# FastAPI Monolithic Web Application


## Objective:
Develop a `monolithic` web application using `FastAPI` with `JWT` authentication. The application should load and store videos on local `S3` storage (or use `AWS` if you have this), respond with video descriptions to the `frontend` using `REST` and `Jinja2`, all within `Docker` containers.

Use `Poetry` for package management, `PostgreSQL` as the main database with async database sessions using asyncpg, `Redis` as the cache database, `Alembic` for migrations, `SQLAlchemy` for `Pydantic` models with databases.

Write `GitHub Actions` pipelines for running tests in pull requests, which will launch `Docker Compose` with test coverage.


### Requirements:
1. **Poetry:**
    - Use Poetry for managing Python dependencies.
    - Keep _pyproject.toml_ clean and research how to separate different depends groups such as _dev_ (local), _app_, _test_, etc, and how to load specific deps groups in `Docker`.

2. **Linters:**
    - `Flake8` - linter.
    - `Blake` - code formatter.
    - `Isort` - import formatter.
    - `MyPy` - static analyzer.

3. **FastAPI Application:**
    - Develop a `monolithic` application to handle all functionalities (e.g., user management, video management).

4. **Dockerization:**
    - Dockerize the entire application.
    - Use containers for the application, `PostgreSQL` databases, `Redis`.
    - Explore using `Docker Compose` for containerization in a local development environment.
    - Read about `Multi-stage` and keep your `Docker` images as light as you can.

5. **Database Integration:**
   - Integrate `PostgreSQL` as the main database for storing video data.
    - Utilize `asyncpg` for async database sessions within the application.
    - Think about how to `design` database schemas and how they should `relate` to each other.

6. **Migrations with Alembic:**
    - Implement database migrations using async `Alembic`.

7. **Pydantic Models with SQLAlchemy:**
    - Use SQLAlchemy for database operations with `Pydantic` models.
    - Use Pydantic schemas as a response from the server.

8. **JWT Authentication:**
    - Implement `JWT` authentication.

9. **RESTful API Endpoints:**
    - Design `RESTful API` endpoints to interact with video and user data.
    - Include endpoints for listing, uploading, updating, and deleting videos and users.
    - All endpoint must be declared using `Pydantic` as a return models (look for FastAPI doc).
    - **Mandatory** Endpoints with any prefix you will use:
      + _health_ - _GET_ request should return a `json` with some hello from app and 200 status code.
      + _home_ - _GET_ request should return a "🦄" as html page.
      + _docs_ - _GET_ request should return a `Swagger` API documentation.

10. **Video and User CRUD Operations:**
    - Implement _CRUD_ (Create, Read, Update, Delete) operations for videos and users within the application.

11. **Local S3 Integration:**
    - Integrate local `S3` storage to allow uploading and retrieval of videos.

12. **Unit Tests and Integration Tests:**
    - Use `Pytest` and `Coverage` libs.
    - Write `unit tests` for any function or method.
    - Write `integration tests` to check full application logic.
    - Ensure all tests run using `Docker Compose` to simulate the entire application environment.

13. **GitHub Actions:**
    - Set up `GitHub Actions` pipeline for launching Python analyzers.
    - Set up pipelines also for running unit tests and system tests in pull requests.

14. **Jinja2 Templates:**
    - Create `Jinja2` templates for rendering video descriptions on the frontend within application.

15. **Celery Task Scheduler:**
    - Implement `Celery` to schedule any daily events at you choice


### Additional Challenges (Optional):
1.  **Makefile:**
   - Research how to use `Makefile` to simplify running commands in th project.

2.  **Pre-commits:**
    - What is `pre-commits` and how use it?

3. **Advanced Video Features:**
    - Implement features like video categorization, tags, and search functionality.
   - Use pagination and filtering parameters (`Pydantic` to the rescue).

4. **User Authentication:**
    - Extend authentication to include user accounts with _roles_ (admin, regular user).

5. **User Roles:**
    - Add user _roles_ such as _admin_ (able to do everything), _manager_ (update videos), _user_ (only get videos).

6. **Cache:**
    - Try to think of a way to use `Redis`.

7. **Container Orchestration (Extra hight level):**
    - Explore using `Kubernetes` for container orchestration in a local development environment. Can start with `minikube`.



### Submission:
- All Python code **MUST** be _typed_ (the `typing` module to your rescue).
- Implement the project according to the `PEP8` standard should be described in the `tool` section of the _pyproject.toml_ for linters with some modifications:
    + String length should be 120 characters.
    + Count of lines after import should be 2.
    + The rest is by specification.
- `Pytest` and `Coverage` configs also should be in in the `tool` section of the _pyproject.toml_.
- Commit style, [click](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/). Commits should contain small logical portions of the code being modified. A clear commit name is required, descriptions within commits are welcome. The commit header should be up to 50 characters and the description up to 72 characters, [read more](https://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting).
- Branch style, [click](https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf#:~:text=own%20development%20cycle.-,Git%20Flow,-The%20Git%20Flow). It is suggested to use GitFlow. Don't forget to delete merged or close branches based on PR status. Development should be done in separate branches, it is not allowed to commit or merge changes directly into _master_ or _develop_.
- Commits, branches and PR's should contain small pieces of separate logic so that it can be revisited. For example, how to decompose and get started (documentation should also be updated and up to date):
  + The first PR would be enough to see poetry installed and a project structure created with a basic fastapi initialization and a first test that verifies that endpoint returns a response.
  + The second PR can only include linters.
  + The third PR involves the use of docker.
- Try to follow all [OOP](https://realpython.com/python3-object-oriented-programming/) & [design](https://www.boldare.com/blog/kiss-yagni-dry-principles/) principles.
- Submit the codebase along with a detailed README explaining how to set up and run the monolithic application, any additional features implemented, and any challenges faced. [Here is](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) a good cheat-list how to style documentation.
- Fork this repository and do your development there.


### Note:
- Use Python 3.10 or above.
- Feel free to use any additional libraries or tools you find suitable for the task.
- You can draw the _database_ schemas and _application_ schemas [here](https://app.diagrams.net/).
- FastAPI best practices [one](https://github.com/zhanymkanov/fastapi-best-practices), [two](https://github.com/Tishka17/fastapi-template/tree/master/src/app) (look how to use protocols).
- Try decomposing tasks into chunks and branches as described above.
- All `highlighted` words should be read in the documentation or familiarized with what they are.
- Follow best practices in terms of code readability, structure, and documentation.


### Suggested project structure:
```
.
├── .github/
│   └── workflows/
│       └── test.yaml
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── user/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── router.py
│   │   │   │   ├── service.py
│   │   │   │   └── views.py
│   │   │   ├── __init__.py
│   │   │   └── web.py
│   │   ├── core/
│   │   │   ├── protocols/
│   │   │   │   └── __init__.py
│   │   │   ├── schemas/
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── infrastructure/
│   │   │   ├── database/
│   │   │   │   ├── models/
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── postgres.py
│   │   │   ├── __init__.py
│   │   │   └── config_loader.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── templates/
│   │   └── README.md
│   ├── Dockerfile
│   ├── README.md
│   └── __init__.py
├── tests/
│   ├── fixtures/
│   │   └── __init__.py
│   ├── integration/
│   │   └── __init__.py
│   ├── unit/
│   │   └── __init__.py
│   ├── .env.test
│   ├── Dockerfile
│   ├── Makefile
│   ├── __init__.py
│   ├── conftest.py
│   └── docker-compose.yml
├── .env.example
├── .env.local
├── .gitignore
├── Makefile
├── README.md
├── docker-compose.yml
├── poetry.lock
└── pyproject.toml
```
