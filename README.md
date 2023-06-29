# Book Author API

## Local Setup

1. Clone repo
    ```shell
    git clone https://github.com/khaled5321/DOCSPERT-backend.git
    ```

2. Create virtual environment
    ```shell
    python -m venv venv
    ```

3. Activate virtual environment
    ```shell
    ./venv/scripts/activate.ps1
    ```

4. Install requirements
    ```shell
    pip install -r requirements.txt
    ```

5. Edit database settings and migrate
    ```shell
    python manage.py migrate
    ```

6. Run server
    ```shell
    python manage.py runserver
    ```

---

## With Docker

Run ```docker-compose up -d --build```