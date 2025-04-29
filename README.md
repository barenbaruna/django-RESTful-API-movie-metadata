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
- Other dependencies listed in `requirements.txt`

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone django-RESTful-API-movie-metadata
   cd django-RESTful-API-movie-metadata
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Existing superuser account. Username:`admin` Password:`admin123`.
   Or create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
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
├── requirements.txt        # Dependencies
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

## 🔄 Integration with Flutter

This backend API is designed to work with a Flutter mobile application. To connect your Flutter app:

1. Use packages like `http` or `dio` to make API requests
2. Implement JWT token storage using `flutter_secure_storage`
3. Create model classes that match the API response structure
4. Use state management solutions (Provider, Bloc, etc.) to handle API data

Example Flutter API service:
```dart
class MovieApiService {
  final String baseUrl = 'https://your-api-domain.com/api';
  final storage = FlutterSecureStorage();
  
  Future<List<Movie>> getMovies() async {
    final token = await storage.read(key: 'auth_token');
    final response = await http.get(
      Uri.parse('$baseUrl/films/'),
      headers: {
        'Authorization': 'Token $token',
        'Content-Type': 'application/json',
      },
    );
    
    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body)['data'];
      return data.map((json) => Movie.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load movies');
    }
  }
  
  // Additional API methods...
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
   pip install gunicorn
   gunicorn movie_project.wsgi:application
   ```

### Docker Deployment
A Dockerfile is provided for containerized deployment.

## ❓ Troubleshooting

### Common Issues
- **API Authentication Errors**: Check that you're using the correct token format
- **Serialization Errors**: Ensure your request body matches the required fields
- **Permission Denied**: Verify user roles (author vs visitor) for restricted endpoints

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

[MIT License](LICENSE) - Feel free to use and modify this project for your own purposes.
