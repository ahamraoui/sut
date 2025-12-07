Feature: Confirmer la commande du panier
  En tant qu'internaute authentifié sur la plateforme,
  Je souhaite confirmer la commande du contenu de mon panier
  Afin d’en réaliser le paiement

  Scenario: Confirmer un panier avec au moins un article
    Given l'internaute est authentifié et a au moins un article dans son panier
    When il accède à la page "Mon panier"
    And il clique sur le bouton "Confirmer le panier"
    Then le montant total, les remises éventuelles et le montant net à payer s'affichent
    And le bouton "Réaliser mon paiement" est actif

  Scenario: Tenter de confirmer un panier vide
    Given l'internaute est authentifié et son panier est vide
    When il accède à la page "Mon panier"
    Then le formulaire "Mon panier" ne s'affiche pas

