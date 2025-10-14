# DUET GRID v2.1-pre — Starter Bundle

Zawartość:
- `openapi.yaml` — Gateway API
- `schemas/` — JSON Schemas (audit, kpi, agent.run)
- `docker-compose.yml` + `compose.override.yml` — MVP lokalnie
- `seeds/` — próbki danych (PV, faktury, granty)
- `grafana/dashboards/duet-kpi-dashboard.json` — dashboard KPI

## Szybki start
```bash
cd duet-grid-v2.1-pre
docker compose -f docker-compose.yml -f compose.override.yml up -d
curl http://localhost:8080/status
```

## Walidacja kontraktów (przykład)
- `schemas/duet.audit.decision.v1.json`
- `schemas/duet.kpi.tick.v1.json`
- `schemas/duet.command.agent.run.v1.json`

## Struktura BUS (NATS/Kafka)
- `duet.command.*`, `duet.event.*`, `duet.audit.*`, `duet.kpi.*`, `duet.alert.*`, `duet.dna.*`

## Uwaga
Obrazy `duet/*:2.1-pre` są placeholderami — podłącz tutaj swoje implementacje agentów i gatewaya.
