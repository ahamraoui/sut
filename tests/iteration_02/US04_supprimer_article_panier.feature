Feature: Supprimer un article du panier
  En tant qu'internaute authentifié sur la plateforme,
  Je souhaite supprimer un article enregistré dans mon panier
  Afin de le retirer de ma commande en cours

  Scenario: Supprimer un article du panier
    Given l'internaute est authentifié et a un article dans son panier
    When il accède à la page "Mon panier"
    Then la liste des articles du panier s'affiche
    When il clique sur le lien "-1" pour un article
    And il confirme la suppression
    Then la quantité de l'article est décrémentée ou l'article est supprimé si quantité = 0
    And si le panier est vide, un message informe que le panier est supprimé

