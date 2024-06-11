from get_number import extract_number
from selenium_whatsapp import send_whatsapp_message

numbers_list = []
numbers_list_converted = []
excluded_numbers = []

message = "Oi, prof! Tudo bem?! Eu sou a profa Marina, peguei seu número no grupo da DRE Metropolitana! Eu era de Cuiabá e atualmente estou no Paraná desenvolvendo minha pesquisa de doutorado com os docentes da rede estadual de MT! Você pode me ajudar com 5min do seu tempo respondendo ao formulário de pesquisa? É rapidinho, eu juro!! O link é do formulário Google:"
link = "https://docs.google.com/forms/d/e/1FAIpQLSeCsytjpURRLgiEClRggardOoCiCeWbP-MBwyq5ELwMJKgWQA/viewform"
extract_number(numbers_list, numbers_list_converted, excluded_numbers)
send_whatsapp_message(numbers_list_converted, message, link)