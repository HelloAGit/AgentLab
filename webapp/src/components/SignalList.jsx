import React, { useEffect, useState } from "react";
import { fetchSignals } from "../api/backend";

export default function SignalList() {
  const [signals, setSignals] = useState([]);
  useEffect(() => {
    const id = setInterval(async () => {
      const s = await fetchSignals();
      setSignals(s);
    }, 60000); // update every 60s to match feed tick
    return () => clearInterval(id);
  }, []);
  return (
    <div>
      <h3>Signals</h3>
      <ul>
        {signals.map((sig) => (
          <li key={sig.timestamp + sig.fixture_id}>
            {sig.fixture_id} {sig.pct_change.toFixed(3)}
          </li>
        ))}
      </ul>
    </div>
  );
}
