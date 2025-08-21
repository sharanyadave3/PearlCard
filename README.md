# PearlCard Fare Calculator

This repository provides an end‑to‑end solution for the **PearlCard** case study.  It
includes a Python backend for fare calculations and a React frontend for user
interaction, along with accompanying unit tests for both layers.

## Repository Structure

```
pearlcard_solution/
├── backend          # Flask service and fare calculation logic
│   ├── app.py
│   ├── data
│   │   └── fares.json
│   ├── models.py
│   ├── services.py
│   ├── tests
│   │   └── test_api.py
│   ├── requirements.txt
│   └── README.md
├── frontend         # React application for the user interface
│   ├── public
│   │   └── index.html
│   ├── src
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── components
│   │   │   ├── JourneyForm.js
│   │   │   ├── JourneyInputRow.js
│   │   │   └── ResultsTable.js
│   │   └── services
│   │       └── api.js
│   ├── tests
│   │   └── App.test.js
│   ├── package.json
│   └── README.md
└── README.md        # High‑level overview and getting started guide
```

## Getting Started

The solution is divided into two parts—backend and frontend—each with its own
README file containing detailed instructions.  To get up and running quickly:

1. **Start the backend**:
   - Follow the steps in `backend/README.md` to set up a Python virtual
     environment, install dependencies, and run the Flask server on
     `localhost:8000`.

2. **Start the frontend**:
   - Follow the steps in `frontend/README.md` to install Node dependencies and
     launch the React development server at `localhost:3000`.

3. Navigate to <http://localhost:3000> in your browser.  Enter up to 20
   journeys and click **Calculate Fare** to fetch results from the API.  The
   app will display the fare for each trip and the total daily fare.

## Key Features

* **Modular architecture** adhering to SOLID principles.  Business logic is
  isolated from transport layers, making it trivial to swap out data sources
  or extend the rules without rewriting the API.
* **Configurable fare rules** stored in a JSON file for ease of maintenance
  and localisation.
* **Comprehensive unit tests** for both API and UI components using pytest
  and React Testing Library.
* **CORS enabled** on the backend to support cross‑origin requests from the
  frontend during development.

## Extensibility

The solution has been designed with future growth in mind.  Additional zones
can be added simply by updating `backend/data/fares.json` with new
combinations.  If fare rules become more complex (e.g. peak/off‑peak pricing
or daily caps), new strategy classes can be created and injected into the
calculator without changing the existing API contract.
