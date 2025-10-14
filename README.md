# DUET GRID v2.1-pre — Enterprise Add-on

Dodatki klasy enterprise:
- Rozszerzone schematy JSON (trade, grants, petlive, ui, life, safety)
- Mock-service (Python/Node) do testów end-to-end
- Pipeline CI (GitHub Actions) z walidacją kontraktów, smoke-testem i SBOM

## Uruchomienie lokalne
```bash
docker compose up -d --build
curl -X POST http://localhost:8081/run -H "Content-Type: application/json" -d '{"agent":"PV-Optimizer","payload":{"test":true}}'
```

## Integracja z repo GitHub
- Skopiuj `.github/workflows/ci.yml` do repo.
- Push → zakładka Actions rozpocznie CI (walidacja schemas vs seeds + SBOM).

## Tematy BUS (NATS/Kafka)
- duet.command.agent.run.v1
- duet.event.status.update.v1
- duet.kpi.tick.v1
- duet.audit.decision.v1
- duet.alert.safety.v1
- duet.dna.update.v1
- duet.trade.signal.v1
- duet.grant.match.v1
- duet.petlive.match.v1
- duet.ui.update.v1
- duet.life.plan.v1

## Noty operacyjne
- Wszystkie schematy są forward-compatible (opcjonalne pola).
- Dodając nowe wersje, stosuj sufiks `.vN` i zachowuj kompatybilność wsteczną.
