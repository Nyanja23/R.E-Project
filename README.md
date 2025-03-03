
# Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Nyanja23/task-tracker.git
    cd task-tracker
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Access the admin panel at `http://127.0.0.1:8000/admin/`.

## Features

- User authentication and profile management.
- Task creation, editing, and deletion.
- Task activity tracking.
- Responsive design using Bootstrap.

## Project Files

- [manage.py](http://_vscodecontentref_/20): Django's command-line utility for administrative tasks.
- [settings.py](http://_vscodecontentref_/21): Django settings for the project.
- [urls.py](http://_vscodecontentref_/22): URL configuration for the project.
- [wsgi.py](http://_vscodecontentref_/23): WSGI configuration for the project.
- [asgi.py](http://_vscodecontentref_/24): ASGI configuration for the project.
- [models.py](http://_vscodecontentref_/25): Database models for the application.
- [views.py](http://_vscodecontentref_/26): Views for handling HTTP requests.
- [urls.py](http://_vscodecontentref_/27): URL configuration for the [base](http://_vscodecontentref_/28) app.
- [index.html](http://_vscodecontentref_/29): HTML template for the home page.
- [style.css](http://_vscodecontentref_/30): Custom CSS styles.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any inquiries, please contact [nuwaherezapeter34@gmail.com]
