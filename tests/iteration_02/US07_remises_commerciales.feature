Feature: Remises commerciales sur la commande
  En tant qu'internaute authentifié sur la plateforme,
  Je souhaite profiter de remises commerciales attribuées selon certaines conditions
  Afin que le montant de ces remises soit déduit du montant total de ma commande

  Scenario: Remise 10% pour ancienneté et commandes
    Given l'internaute est inscrit depuis plus de 6 mois et a déjà réalisé 3 commandes pour 300€
    When il passe une nouvelle commande
    Then une remise de 10% est appliquée

  Scenario: Remise 5% pour 1ère commande et département du mois
    Given l'internaute réalise sa 1ère commande et réside dans un département du mois
    When il passe une commande
    Then une remise de 5% est appliquée

  Scenario: Remise 7% pour VIP et ancienneté
    Given l'internaute est inscrit depuis plus de 12 mois, a déjà réalisé 500€ d'achats et est VIP
    When il passe une commande
    Then une remise de 7% est appliquée

  Scenario: Remise 5% pour plus de 10 commandes dans l'année
    Given l'internaute a réalisé plus de 10 commandes dans l'année
    When il passe une commande
    Then une remise de 5% est appliquée

  Scenario: Remise code PROMO prioritaire
    Given l'internaute renseigne un code PROMO lors de la confirmation du panier
    When il passe une commande
    Then la remise associée au code PROMO est appliquée et prioritaire

  Scenario: Remises non cumulables
    Given plusieurs conditions de remises sont réunies
    When il passe une commande
    Then une seule remise est appliquée, la plus prioritaire

