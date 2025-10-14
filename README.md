# Pytest_profesional
Good Testing Practices(Pytest)

📄 Description

Pytest Profesional is a Django project with advanced testing and modular architecture.
The environment is isolated, reproducible, and scalable, following enterprise standards, ideal for complex projects and team collaboration.

✨ This project demonstrates best practices, test quality, and technical leadership skills.

🌟 Features

🏗 Modular: apps usuario, libro, biblioteca.

🧪 Tests organized by type:

test_apps/ → model logic and methods.

test_serializers/ → serializer tests.

test_views/ → endpoint and view tests.

🔄 Professional testing workflow:

Faker → FactoryBoy → Fixtures → Mocks → Tests


✅ Isolated and reproducible tests, no hard-coded data.

👥 Ready for teams and complex projects.

## 🗂 Project Structure
```text
pytest_profesional/                 <- Project root
├── .venv/                          <- Virtual environment
├── pytest_profesional/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── usuario/
│   │   ├── __init__.py
│   │   ├── models.py             <- User model
│   │   ├── context_manager.py    <- UserContextManager
│   │   ├── serializers.py        <- UserSerializer
│   │   ├── views.py              <- User CRUD views
│   │   └── urls.py
│   ├── libro/
│   │   ├── __init__.py
│   │   ├── models.py             <- Book model
│   │   ├── context_manager.py    <- BookContextManager
│   │   ├── serializers.py        <- BookSerializer
│   │   ├── views.py              <- Book CRUD views
│   │   └── urls.py
│   └── biblioteca/
│       ├── __init__.py
│       ├── models.py             <- Library model
│       ├── context_manager.py    <- LibraryContextManager
│       ├── serializers.py        <- LibrarySerializer
│       ├── views.py              <- Library CRUD views
│       └── urls.py
├── tests/
│   ├── conftest.py               <- Global fixtures, Faker, FactoryBoy, Mocks
│   ├── factories/                <- FactoryBoy for models
│   │   ├── usuario_factory.py
│   │   ├── libro_factory.py
│   │   └── biblioteca_factory.py
│   ├── fixtures/                 <- Reusable test data
│   │   ├── usuario_fixtures.py
│   │   ├── libro_fixtures.py
│   │   └── biblioteca_fixtures.py
│   ├── mocks/                     <- Reusable mocks for services/dependencies
│   │   ├── usuario_mock.py
│   │   ├── libro_mock.py
│   │   └── biblioteca_mock.py
│   ├── test_apps/                <- Unit tests for models and logic
│   │   ├── test_usuario.py
│   │   ├── test_libro.py
│   │   └── test_biblioteca.py
│   ├── test_serializers/         <- Serializer tests
│   │   ├── test_usuario_serializer.py
│   │   ├── test_libro_serializer.py
│   │   └── test_biblioteca_serializer.py
│   ├── test_views/               <- Views and endpoint tests
│   │   ├── test_usuario_view.py
│   │   ├── test_libro_view.py
│   │   └── test_biblioteca_view.py
│   └── reports/                  <- Test and coverage reports
│       ├── coverage.xml
│       ├── htmlcov/
│       │   └── index.html
│       └── pytest_report.log
├── manage.py
└── requirements.txt

⚡ Professional Testing Workflow

🎲 Global Faker – Realistic data with custom providers.

🏭 FactoryBoy – Controlled model instances.

🧩 Fixtures – Reusable test data.

🛡 Mocks – Isolation of external services and dependencies.

🧪 Tests – Consume only fixtures and mocks, ensuring full isolation.

🎯 Professionalism

✅ Isolated and reliable tests, following enterprise best practices.

🏗 Modular and scalable architecture, ready for multiple apps and teams.

👨‍💻 Demonstrates technical leadership and standardized testing processes.
