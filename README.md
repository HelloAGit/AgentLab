# AgentLab
AgentLab
AgentLab/
├─ README.md
├─ LICENSE
├─ .env.example
├─ docker-compose.yml
├─ infra/
│  ├─ solana/
│  │  ├─ program/                # on-chain program (Rust) or client scripts
│  │  └─ deploy_devnet.sh
├─ backend/
│  ├─ monitor/
│  │  ├─ main.py
│  │  ├─ txline_client.py
│  │  ├─ detector.py
│  │  └─ requirements.txt
│  ├─ agents/
│  │  ├─ agent_base.py
│  │  ├─ agent_momentum.py
│  │  ├─ agent_meanrev.py
│  │  └─ run_agents.sh
│  ├─ arena/
│  │  ├─ arena_server.py
│  │  ├─ matcher.py
│  │  └─ onchain_client.py
│  └─ common/
│     ├─ models.py
│     └─ utils.py
├─ webapp/
│  ├─ package.json
│  ├─ src/
│  │  ├─ App.jsx
│  │  ├─ components/
│  │  │  ├─ Dashboard.jsx
│  │  │  ├─ SignalList.jsx
│  │  │  └─ ArenaPanel.jsx
│  │  └─ api/
│  │     └─ backend.js
│  └─ public/
└─ tests/
   ├─ test_detector.py
   ├─ test_agents.py
   └─ test_arena.py
