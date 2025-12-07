Feature: Déconnexion de la plateforme
  En tant qu'internaute authentifié,
  Je souhaite me déconnecter de la plateforme
  Afin de sécuriser mon compte

  Scenario: Déconnexion réussie
    Given l'internaute est authentifié et sur son espace personnel
    When il clique sur le bouton "Déconnexion"
    Then il est redirigé vers la page de connexion
    And un message de confirmation de déconnexion s'affiche

