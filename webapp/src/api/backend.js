export async function fetchSignals() {
  const res = await fetch("/api/signals");
  return res.json();
}

export async function fetchFixtures() {
  const res = await fetch("/api/fixtures");
  return res.json();
}
