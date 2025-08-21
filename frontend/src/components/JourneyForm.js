import React from 'react';
import JourneyInputRow from './JourneyInputRow';

const JourneyForm = ({ journeys, onChange, onAdd, onRemove, onSubmit }) => {
  return (
    <form onSubmit={onSubmit} className="journey-form">
      {journeys.map((journey, index) => (
        <JourneyInputRow
          key={index}
          index={index}
          journey={journey}
          onChange={onChange}
          onRemove={onRemove}
          disabledRemove={journeys.length <= 1}
        />
      ))}
      <div className="form-actions">
        {journeys.length < 20 && (
          <button type="button" onClick={onAdd} aria-label="Add Journey">
            Add Journey
          </button>
        )}
        <button type="submit">Calculate Fare</button>
      </div>
    </form>
  );
};

export default JourneyForm;