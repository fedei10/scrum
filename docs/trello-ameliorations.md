# Améliorations proposées au Trello existant

**Ne pas recréer ni déplacer rétroactivement les cartes de l'équipe sans vérification.**

## Conserver les colonnes existantes

- Backlog : 6 Epics visibles sur la capture (elles regroupent des fonctionnalités).
- To Do : 4 tâches visibles sur la capture.
- Doing : 4 tâches visibles sur la capture.
- Test/Review : 3 tâches visibles sur la capture.
- Done : 4 tâches *déclarées* terminées sur la capture (non auditées).

## Policies proposées pour les prochaines itérations

- **Doing : WIP <= 2.** Une tâche entre dans Doing si ses critères d'acceptation sont clairs et si de la capacité est disponible.
- **Test/Review : WIP <= 2.** Une tâche ne passe en Done que si la DoD est satisfaite.
- **Priorité aux blocages :** avant de commencer une nouvelle tâche, résoudre les blocages ou terminer les tâches déjà ouvertes.
- **Tâches bloquées :** ajouter l'étiquette Bloqué + cause et date dans un commentaire.
- **Traçabilité :** lien vers commit, PR, résultats de tests/CI et décision de revue.

Ces limites sont des **propositions nouvelles**, pas des pratiques déjà attestées. La capture d'origine montre un WIP de 4 dans Doing et de 3 dans Test/Review.

## Cartes techniques complémentaires (sans dupliquer les cartes métier)

- XP-01 — Préparer le kata et les tests smoke (semaine 1).
- XP-02 — Configurer et vérifier le pipeline CI (semaine 1).
- XP-03 — Documenter le TDD sur `E2 > room capacity` (semaine 2, carte liée existante).
- XP-04 — Journal des séances de pairing (semaine 2).
- XP-05 — Mesurer les itérations classiques et XP (semaine 2).
- XP-06 — Analyser dette technique et flux + rétro (semaine 3).

## Format d'un commentaire de preuve

- Date :
- Réalisé par :
- Hypothèse / critère d'acceptation :
- Résultat réellement observé :
- Lien commit / PR / CI :
- Décision / action suivante :
