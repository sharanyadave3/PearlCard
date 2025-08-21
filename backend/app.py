

from __future__ import annotations

import os
from typing import Any, Dict, List, Tuple

from flask import Flask, jsonify, request
from flask_cors import CORS

from .models import Journey
from .services import FareRulesRepository, FareCalculator


def create_app() -> Flask:
    """Application factory for the PearlCard Flask app."""
    app = Flask(__name__)
    CORS(app)  # allow all origins during development

    # Initialise the fare rule repository and calculator
    # Build absolute path to the JSON rules file
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'fares.json')
    repo = FareRulesRepository(json_path=json_path)
    calculator = FareCalculator(repo)

    @app.route('/calculate-fares', methods=['POST'])
    def calculate_fares() -> Tuple[Any, int]:

        journeys_data = request.get_json(force=True, silent=True)
        if not isinstance(journeys_data, list):
            return jsonify({'error': 'Payload must be a JSON array.'}), 400
        journeys: List[Journey] = []
        for item in journeys_data:
            try:
                from_zone = int(item.get('from_zone'))
                to_zone = int(item.get('to_zone'))
                if from_zone <= 0 or to_zone <= 0:
                    raise ValueError
                journeys.append(Journey(from_zone, to_zone))
            except Exception:
                return jsonify({'error': 'Each journey must include positive integer from_zone and to_zone values.'}), 400
        try:
            results, total = calculator.calculate_journeys(journeys)
        except ValueError as exc:
            return jsonify({'error': str(exc)}), 400
        return jsonify({'journeys': results, 'total_fare': total}), 200

    return app


if __name__ == '__main__':
    # When run directly, create the app and serve it on the configured port
    app = create_app()
    port = int(os.environ.get('PORT', '8000'))
    app.run(host='0.0.0.0', port=port, debug=True)