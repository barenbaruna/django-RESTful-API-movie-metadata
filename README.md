# Movie Metadata API

A comprehensive RESTful API for movie metadata management built with Django REST Framework. This backend service powers a Flutter-based mobile application for browsing and rating movies.

## 📑 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Data Models](#-data-models)
- [Authentication](#-authentication)
- [API Endpoints](#-api-endpoints)
- [Response Formats](#-response-formats)
- [Flutter Front-End Repository](#-flutter-front-end-repository)
- [Integration with Flutter](#-integration-with-flutter)
- [Development](#-development)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features

- User authentication and authorization with differentiated roles (authors and visitors)
- CRUD operations for movie metadata management
- Rich relationships between movies and related entities (actors, directors, etc.)
- Rating system with automatic average rating calculation
- User profile management with avatar support
- RESTful API design principles for easy integration

## 📋 Requirements

- Python 3.8+
- Django 4.2.1
- Django REST Framework 3.14.0
- Pillow 9.5.0 (for image processing)
- Other dependencies listed in `req.txt`

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd movie-fix
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r req.txt
   ```

4. Configure environment variables (create a `.env` file if needed):
   ```
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 🏗️ Project Structure

The project follows a standard Django application structure:

```
movie-fix/
├── api/                    # API application
│   ├── serializers.py      # Data serialization
│   ├── views.py            # API endpoints
│   └── urls.py             # URL routing
├── movie_app/              # Core application
│   ├── models.py           # Data models
│   ├── admin.py            # Admin configuration
│   └── migrations/         # Database migrations
├── movie_project/          # Project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── media/                  # User-uploaded files
├── static/                 # Static files
├── manage.py               # Django management script
├── req.txt                 # Dependencies
└── README.md               # Project documentation
```

## 📊 Data Models

The application has the following data models:

- **User**: Extended Django user with author/visitor roles and custom permissions
- **Profile**: User profile with personal information, biography, and avatar
- **Film**: Core movie entity with title, description, release year, and relationships
- **Aktor**: Actor information with name and relationships to films
- **Sutradara**: Director information with name and relationships to films
- **Genre**: Movie genres classification
- **Negara**: Countries of origin for movies
- **Bahasa**: Languages available for movies
- **Rating**: User ratings for movies with numerical score system

## 🔐 Authentication

The API uses token-based authentication. Users can register as either authors (content creators) or visitors (content consumers):

1. Register a new user (`/api/register/`)
2. Login to receive an authentication token (`/api/login/`)
3. Include the token in the Authorization header for protected endpoints:
   ```
   Authorization: Token <your_token_here>
   ```

## 🌐 API Endpoints

The API provides the following endpoints:

### Authentication
- `POST /api/login/` - User login with username and password
- `POST /api/register/` - Register new users (authors or visitors)
- `POST /api/logout/` - User logout (invalidates token)

### Profiles
- `GET /api/profiles/` - List all user profiles
- `GET /api/profiles/<id>/` - Retrieve a specific profile
- `PUT /api/profiles/<id>/` - Update a profile (authenticated user's own profile)
- `PATCH /api/profiles/<id>/` - Partially update a profile

### Movies
- `GET /api/films/` - List all movies with filtering and pagination
- `POST /api/films/` - Create a new movie (author authorization required)
- `GET /api/films/<id>/` - Retrieve a specific movie with details
- `PUT /api/films/<id>/` - Update a movie (author authorization required)
- `PATCH /api/films/<id>/` - Partially update a movie (author authorization required)
- `DELETE /api/films/<id>/` - Delete a movie (author authorization required)

### Ratings
- `POST /api/ratings/` - Rate a movie (authenticated users)
- `GET /api/ratings/` - List all ratings
- `GET /api/ratings/user/<user_id>/` - Get ratings by a specific user
- `GET /api/ratings/film/<film_id>/` - Get ratings for a specific film

### Resource Endpoints
Each of these resource types has standard CRUD endpoints:
- `/api/actors/` - Manage actors
- `/api/directors/` - Manage directors
- `/api/genres/` - Manage genres
- `/api/countries/` - Manage countries
- `/api/languages/` - Manage languages

## 📦 Response Formats

API responses follow consistent JSON formatting:

### Success Response:
```json
{
  "status": "success",
  "data": { ... }
}
```

### Error Response:
```json
{
  "status": "error",
  "message": "Error description",
  "code": "ERROR_CODE"
}
```

### Film Object Example:
```json
{
  "id": 1,
  "title": "Inception",
  "description": "A thief who steals corporate secrets...",
  "release_year": 2010,
  "sutradara": ["Christopher Nolan"],
  "aktor": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
  "genre": ["Sci-Fi", "Action"],
  "negara": ["United States"],
  "bahasa": ["English"],
  "average_rating": 4.8,
  "poster": "http://example.com/media/posters/inception.jpg"
}
```

## 🔗 Flutter Front-End Repository

This Django backend is paired with a Flutter front-end application. The complete movie application consists of:

- **Backend**: This Django REST API repository
- **Frontend**: Flutter mobile application

### Flutter Repository

You can find the Flutter front-end code at:

[Movie App Flutter Repository](https://github.com/barenbaruna/flutter_movie)

### Complete Application Setup

To run the complete application with both frontend and backend:

1. Set up this backend repository following the installation steps above
2. Clone and set up the Flutter repository following its README instructions
3. Configure the Flutter app to connect to your running backend server

## 🔄 Integration with Flutter

The integration between this Django backend and the Flutter frontend provides a seamless movie browsing and rating experience:

1. **Authentication Flow**: 
   - The Flutter app uses the login/register endpoints to authenticate users
   - Authentication tokens are securely stored on the mobile device
   - Different UI elements are displayed based on user role (author/visitor)

2. **Data Flow**:
   - The Flutter app fetches and displays movie data, actors, directors, etc.
   - Authors can create and manage movie content through the app
   - Users can browse movies, view details, and submit ratings

3. **Real-time Experience**:
   - Rating changes are immediately reflected in average ratings
   - New content becomes available across all app instances

Example Flutter-Django integration code for authentication:

```dart
Future<bool> login(String username, String password) async {
  final response = await http.post(
    Uri.parse('$apiBaseUrl/api/login/'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'username': username,
      'password': password,
    }),
  );
  
  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    await secureStorage.write(key: 'auth_token', value: data['token']);
    return true;
  }
  return false;
}
```

## 👨‍💻 Development

### Running Tests
```bash
python manage.py test
```

### Code Style
This project follows PEP 8 guidelines. Before committing, run:
```bash
flake8 .
black .
```

### Adding New Features
1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Implement your changes with tests
3. Submit a pull request

## 🚢 Deployment

### Production Setup
1. Set environment variables for production:
   ```
   DEBUG=False
   SECRET_KEY=your_secure_key
   ALLOWED_HOSTS=yourdomain.com
   DATABASE_URL=postgres://user:password@host:port/database
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Deploy using gunicorn and nginx:
   ```bash
   gunicorn movie_project.wsgi:application
   ```

### Docker Deployment
A Dockerfile is provided for containerized deployment.

## ❓ Troubleshooting

### Common Issues
- **API Authentication Errors**: Check that you're using the correct token format
- **Serialization Errors**: Ensure your request body matches the required fields
- **Permission Denied**: Verify user roles (author vs visitor) for restricted endpoints

### Logging
Check the server logs for detailed error information:
```bash
tail -f logs/django.log
```

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

[MIT License](LICENSE) - Feel free to use and modify this project for your own purposes.
