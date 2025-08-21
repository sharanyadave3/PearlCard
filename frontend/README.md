# PearlCard Frontend

This directory contains the React application for interacting with the PearlCard
fare calculator.  It provides a simple user interface for commuters to enter
their daily journeys and view the resulting fares.

## Requirements

* [Node.js](https://nodejs.org/) (version 16 or higher)
* npm (comes bundled with Node.js)

## Setup

1. Open a terminal and navigate into the `frontend` folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

## Configuration

The frontend expects the backend API to be available at
`http://localhost:8000` by default.  If your backend runs on a different
hostname or port, create a `.env` file in the `frontend` directory with the
following content:

```
REACT_APP_API_BASE_URL=http://your-backend-host:port
```

React will load this environment variable and use it when constructing API
requests.

## Running the Application

To start the development server, run:

```bash
npm start
```

This will launch the React app at <http://localhost:3000>.  The page will
automatically reload when you make changes to the source code.

## Unit Tests

Unit tests reside in the `tests` directory and leverage `@testing-library/react`
to verify component behaviour.  Run tests with:

```bash
npm test
```

The tests mock out API calls to ensure a fast and deterministic test suite.