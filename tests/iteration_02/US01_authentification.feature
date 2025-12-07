Feature: Authentification sur la plateforme
  En tant qu'internaute,
  Je souhaite m'authentifier sur la plateforme
  Afin d'accéder à mon espace personnel et effectuer des commandes

  Scenario: Authentification réussie
    Given l'internaute est sur la page de connexion
    When il saisit un identifiant et un mot de passe valides
    And il clique sur le bouton "Se connecter"
    Then il est redirigé vers son espace personnel
    And un message de bienvenue s'affiche

  Scenario: Authentification échouée
    Given l'internaute est sur la page de connexion
    When il saisit un identifiant ou un mot de passe invalide
    And il clique sur le bouton "Se connecter"
    Then un message d'erreur s'affiche

