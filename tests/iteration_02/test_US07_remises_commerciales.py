from bhave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("l'internaute est inscrit depuis plus de 6 mois et a déjà réalisé 3 commandes pour 300€")
def step_impl(context):
    # Préparer le contexte utilisateur
    pass

@given("l'internaute réalise sa 1ère commande et réside dans un département du mois")
def step_impl(context):
    pass

@given("l'internaute est inscrit depuis plus de 12 mois, a déjà réalisé 500€ d'achats et est VIP")
def step_impl(context):
    pass

@given("l'internaute a réalisé plus de 10 commandes dans l'année")
def step_impl(context):
    pass

@given("l'internaute renseigne un code PROMO lors de la confirmation du panier")
def step_impl(context):
    pass

@given("plusieurs conditions de remises sont réunies")
def step_impl(context):
    pass

@when('il passe une nouvelle commande')
def step_impl(context):
    pass

@when('il passe une commande')
def step_impl(context):
    pass

@then('une remise de 10% est appliquée')
def step_impl(context):
    pass

@then('une remise de 5% est appliquée')
def step_impl(context):
    pass

@then('une remise de 7% est appliquée')
def step_impl(context):
    pass

@then('la remise associée au code PROMO est appliquée et prioritaire')
def step_impl(context):
    pass

@then('une seule remise est appliquée, la plus prioritaire')
def step_impl(context):
    pass

