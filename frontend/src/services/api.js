import axios from 'axios';

// Base URL can be overridden at build time by defining REACT_APP_API_BASE_URL
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

/**
 * Post a list of journeys to the backend and return the calculated fares.
 *
 * @param {Array<{from_zone: number, to_zone: number}>} journeys
 * @returns {Promise<{journeys: Array<{from_zone: number, to_zone: number, fare: number}>, total_fare: number}>}
 */
export async function calculateFares(journeys) {
  const response = await axios.post(`${API_BASE_URL}/calculate-fares`, journeys);
  return response.data;
}