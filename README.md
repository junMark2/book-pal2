# Book Palette

## Description

Book Palette is a book-community platform built using Django REST Framework (DRF) for the backend and Vue.js for the frontend. The application visualizes user reading preferences by assigning colors to book genres, creating personalized color profiles.

## Installation

### Backend Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/junMark2/book-pal2.git
   cd book-pal2/backend
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend` directory and add the following line:
   ```sh
   ALADIN_API_KEY=ttbjhpark9706021328002
   ```

5. Run the initial migrations and start the development server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```sh
   cd ../frontend
   ```

2. Install the required dependencies:
   ```sh
   npm install
   ```

3. Start the development server:
   ```sh
   npm run serve
   ```

## Usage

### Backend

- The backend provides CRUD API endpoints for managing users, books, genres, threads, comments, likes, and color history.
- It also includes an authentication system using DRF Token Authentication or JWT.
- An API endpoint is available to calculate and return a user's representational color based on their color history.

### Frontend

- The frontend includes the following pages:
  - Home: Displays user color summary and recommended books.
  - Books: Provides list and detail views, reading status, and personal notes.
  - Community: Shows thread list and detail views, comments, and likes.
  - User Profile: Visualizes user color profile and reading statistics.
  - Login/Signup: Simple forms for user authentication.

- Each page is integrated with the backend APIs to ensure seamless functionality.
