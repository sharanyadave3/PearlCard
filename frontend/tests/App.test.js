import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from '../src/App';
import * as api from '../src/services/api';

// Mock the API module so tests don't make real HTTP requests
jest.mock('../src/services/api');

describe('PearlCard App', () => {
  beforeEach(() => {
    // Clear previous mock calls
    api.calculateFares.mockReset();
  });

  test('allows adding journeys up to the limit', () => {
    render(<App />);
    const addButton = screen.getByRole('button', { name: /add journey/i });
    // Click the add button once; there should be two rows now (4 inputs)
    fireEvent.click(addButton);
    let inputs = screen.getAllByRole('spinbutton');
    expect(inputs.length).toBe(4);
    // Add journeys until the limit is reached
    for (let i = 0; i < 18; i++) {
      fireEvent.click(addButton);
    }
    // The add button should now be disabled/hidden because 20 journeys exist
    expect(screen.queryByRole('button', { name: /add journey/i })).toBeNull();
  });

  test('displays results after fare calculation', async () => {
    // Arrange mock API response
    api.calculateFares.mockResolvedValue({
      journeys: [
        { from_zone: 1, to_zone: 1, fare: 40 },
        { from_zone: 2, to_zone: 3, fare: 45 },
      ],
      total_fare: 85,
    });
    render(<App />);
    // Fill out first journey
    fireEvent.change(screen.getByLabelText(/from zone/i), { target: { value: '1' } });
    fireEvent.change(screen.getByLabelText(/to zone/i), { target: { value: '1' } });
    // Add a second journey
    fireEvent.click(screen.getByRole('button', { name: /add journey/i }));
    const fromInputs = screen.getAllByLabelText(/from zone/i);
    const toInputs = screen.getAllByLabelText(/to zone/i);
    fireEvent.change(fromInputs[1], { target: { value: '2' } });
    fireEvent.change(toInputs[1], { target: { value: '3' } });
    // Submit the form
    fireEvent.click(screen.getByRole('button', { name: /calculate fare/i }));
    // Wait for the total fare to appear
    const totalCell = await screen.findByText('85');
    expect(totalCell).toBeInTheDocument();
    // Verify that journeys are displayed
    expect(screen.getAllByRole('row').length).toBeGreaterThan(2);
  });
});