# Contributing

1. Fork repo i utwórz branch feature: `feat/<nazwa>`.
2. Dodaj/zmień kontrakty w `schemas/` (tylko dodawaj pola opcjonalnie — forward compatible).
3. Uruchom lokalnie: `docker compose up -d` (BUS + mocki).
4. Upewnij się, że CI (GitHub Actions) przechodzi — walidacja kontraktów i SBOM.
5. PR musi przejść gate'y: ARCH++ → CODE → QA → COMP → (SAFETY) → AUDIT.
