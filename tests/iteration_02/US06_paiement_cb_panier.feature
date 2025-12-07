Feature: Paiement par carte bancaire du panier
  En tant qu'internaute authentifié sur la plateforme,
  Je souhaite réaliser le paiement par carte bancaire de mon panier
  Afin de me faire livrer les articles commandés

  Scenario: Paiement CB avec adresse de livraison renseignée
    Given l'internaute est authentifié, a un panier prêt à payer et une adresse de livraison renseignée
    When il accède à la page de paiement
    And il renseigne les informations de carte bancaire valides
    And il clique sur "Confirmer paiement CB"
    Then le paiement est enregistré et un récapitulatif s'affiche

  Scenario: Paiement CB sans adresse de livraison
    Given l'internaute est authentifié, a un panier prêt à payer et aucune adresse de livraison
    When il accède à la page de paiement
    Then un message popup demande de renseigner l'adresse de livraison et un lien vers "Mon Profil" est affiché

  Scenario: Paiement CB refusé par l'API
    Given l'internaute est authentifié, a un panier prêt à payer et une adresse de livraison renseignée
    When il saisit des informations de carte bancaire invalides
    And il clique sur "Confirmer paiement CB"
    Then un message d'erreur s'affiche et les champs CB sont réinitialisés

