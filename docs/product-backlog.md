# Product Goal et Product Backlog

## Product Goal

Permettre à un utilisateur de planifier et de gérer des réunions de façon simple et fiable, en vérifiant les règles métier essentielles (dont la capacité des salles), avec des retours rapides sur la qualité du code.

## Les 6 Epics visibles dans la capture de l'équipe

- E1 — Authentication
- E2 — Create a meeting
- E3 — Invite participants
- E4 — View meetings
- E5 — Cancel or reschedule a meeting
- E6 — Reminders

## Les 9 User Stories présentes dans le rapport initial

| ID | User story | Priorité initiale |
|---|---|---|
| US01 | Créer un compte pour accéder à l'application | Haute |
| US02 | Créer une réunion (titre, date, heure, durée) | Haute |
| US03 | Consulter la liste de mes réunions | Haute |
| US04 | Annuler une réunion | Haute |
| US05 | Ajouter des participants à une réunion | Haute |
| US06 | Confirmer ou refuser ma participation | Moyenne |
| US07 | Recevoir une notification avant une réunion | Moyenne |
| US08 | Gérer les salles de réunion | Moyenne |
| US09 | Consulter l'historique des réunions | Basse |

**Note de traçabilité :** les 6 Epics Trello ne correspondent pas un-pour-un aux 9 User Stories du rapport. La règle « capacité maximale de salle » apparaît dans une carte détaillée de l'Epic E2 de la capture, sans ligne distincte dans les 9 User Stories.

## Périmètre du kata de démonstration

La semaine 1 fournit uniquement un squelette d'API et un test de santé.
La semaine 2 utilisera la règle « refuser une réunion si le nombre de participants dépasse la capacité de la salle » comme fonctionnalité d'expérimentation XP (et, si utile, une règle comparable pour l'approche classique).
