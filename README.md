# AgentLab
AgentLab — TxLINE Agent Lab
AgentLab is a local-first toolkit and reference implementation for building, testing, and running automated trading agents that monitor TxLINE odds, flag significant odds shifts every 60 seconds, and compete in an Agent vs Agent Arena where opposing strategies place positions that settle on‑chain. The repository contains a monitor, two agent templates, an arena matcher with on‑chain settlement hooks, and a minimal React webapp dashboard.

What this repo contains
Monitor — polls a TxLINE odds feed every 60 seconds, detects sharp movements, logs signals, and publishes them to the Arena and agents.

Agents — two example agents (momentum and mean‑reversion) that subscribe to the same feed and submit opposing intents to the Arena.

Arena — matches opposing intents, records results, and exposes hooks to settle matched positions on a blockchain (Solana devnet example).

Webapp — a lightweight React dashboard that displays live fixtures, signals, agent statuses, and match logs.

Infra — scaffolding and scripts for on‑chain program deployment and local testing.

Tests — unit tests for detector, agents, and matcher logic.

Goals and design principles
Deterministic polling cadence: monitor ticks every 60 seconds to match TxLINE feed cadence.

Signal provenance: every signal is logged with timestamped metadata for audit and backtesting.

Agent parity: both agents read the same feed and operate independently so tournament outcomes reflect strategy performance.

On‑chain settlement hooks: the Arena demonstrates how to call a blockchain client (Solana devnet example) to record or settle matched positions.

Extensible: modular components let you swap detectors, strategies, or the on‑chain program.
