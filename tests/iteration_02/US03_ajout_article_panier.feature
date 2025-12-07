Feature: Ajouter des articles dans le panier
  En tant qu'internaute authentifié sur la plateforme,
  Je souhaite ajouter des articles dans mon panier à partir de la page « Boutique »
  Afin d’en confirmer leur commande

  Scenario: Ajouter un article par code article
    Given l'internaute est authentifié et sur la page "Boutique"
    When il saisit un code article valide dans la barre de recherche
    And il clique sur le bouton "Rechercher"
    Then la liste des articles correspondants s'affiche
    When il clique sur le lien vert "+1" pour un article disponible
    Then l'article est ajouté au panier et le nombre d'articles du panier est incrémenté de 1

  Scenario: Ajouter un article par mot clé
    Given l'internaute est authentifié et sur la page "Boutique"
    When il saisit un mot clé dans la barre de recherche
    And il clique sur le bouton "Rechercher"
    Then la liste des articles correspondants s'affiche
    When il clique sur le lien vert "+1" pour un article disponible
    Then l'article est ajouté au panier

  Scenario: Ne pas pouvoir ajouter un article indisponible
    Given l'internaute est authentifié et sur la page "Boutique"
    When il recherche un article indisponible
    Then le lien "+1" est inactif et de couleur rouge
    When il tente de cliquer sur le lien rouge "+1"
    Then l'article n'est pas ajouté au panier

