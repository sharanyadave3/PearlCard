import React from 'react';

/**
 * A single row in the journey form.  Collects the starting and ending zones
 * for one trip.  Remove button can be disabled when only a single row
 * remains to enforce at least one journey entry.
 */
const JourneyInputRow = ({ index, journey, onChange, onRemove, disabledRemove }) => {
  return (
    <div className="journey-row">
      <label>
        From Zone
        <input
          type="number"
          min="1"
          value={journey.from_zone}
          onChange={(e) => onChange(index, 'from_zone', e.target.value)}
          aria-label="From Zone"
        />
      </label>
      <label>
        To Zone
        <input
          type="number"
          min="1"
          value={journey.to_zone}
          onChange={(e) => onChange(index, 'to_zone', e.target.value)}
          aria-label="To Zone"
        />
      </label>
      <button
        type="button"
        onClick={() => onRemove(index)}
        disabled={disabledRemove}
        aria-label={`Remove journey ${index + 1}`}
      >
        Remove
      </button>
    </div>
  );
};

export default JourneyInputRow;