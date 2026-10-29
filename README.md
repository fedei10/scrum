# XP Meeting Kata — Semaine 1

Mini-projet pédagogique **distinct de l'application d'origine** des coéquipiers. Il reprend le même domaine fonctionnel (gestion de réunions) afin d'étudier Extreme Programming à partir d'une base réellement exécutable.

> **Intégrité académique :** ne pas présenter ce dépôt comme la preuve d'itérations, de commits ou de séances de pairing effectués antérieurement par le groupe. Les simulations des semaines 2 et 3 seront signalées comme telles.

## Objectif de la semaine 1

- Étudier XP et son lien avec Scrum/DevOps (voir le rapport théorique existant).
- Réutiliser le Product Goal / backlog de gestion de réunions.
- Définir une DoD technique.
- Préparer un dépôt Git et une intégration continue minimale.
- Obtenir un premier test automatisé réel sur `/health`.

## Exécuter sur Linux / Ubuntu

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

L'API est sur `http://127.0.0.1:8000` ; la documentation FastAPI est sur `/docs`.

## Créer le dépôt et vérifier la CI GitHub

```bash
git init
git add .
git commit -m "chore: scaffold XP meeting kata with smoke tests and CI"
```

Créer ensuite un dépôt GitHub vide, l'ajouter comme `origin`, puis pousser la branche. Exemple si votre branche locale est `main` :

```bash
git branch -M main
git remote add origin URL_DE_VOTRE_DEPOT
git push -u origin main
```

Ouvrir ensuite l'onglet **Actions** du dépôt et vérifier les résultats du workflow `Python tests`. La présence du fichier `.github/workflows/ci.yml` ne prouve pas à elle seule qu'une CI a été exécutée.

## Documents fournis

- `docs/product-backlog.md` : contexte initial et 9 User Stories.
- `docs/definition-of-done.md` : DoD reproductible.
- `docs/trello-ameliorations.md` : policies et cartes techniques proposées.
- `docs/semaine1-preuves.md` : preuves attendues et état de vérification.
- `docs/semaine1-rapport.tex` : passage LaTeX adaptable après validation.

## Semaine 2 (non réalisée ici)

Comparer une approche avec tests tardifs à une itération TDD sur des règles métier contrôlées. Les métriques réelles seront séparées des données de simulation. Ne pas affirmer que le TDD réduit les bugs sans protocole et sans résultats observés.
