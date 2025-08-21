import React from 'react';

/**
 * Display the calculated fares for each journey in a table.  Shows the
 * cumulative total at the bottom.  When no results are available, the
 * component renders nothing.
 */
const ResultsTable = ({ results }) => {
  if (!results) {
    return null;
  }
  return (
    <div className="results">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>From Zone</th>
            <th>To Zone</th>
            <th>Fare</th>
          </tr>
        </thead>
        <tbody>
          {results.journeys.map((journey, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{journey.from_zone}</td>
              <td>{journey.to_zone}</td>
              <td>{journey.fare}</td>
            </tr>
          ))}
        </tbody>
        <tfoot>
          <tr>
            <td colSpan="3">Total Fare</td>
            <td>{results.total_fare}</td>
          </tr>
        </tfoot>
      </table>
    </div>
  );
};

export default ResultsTable;