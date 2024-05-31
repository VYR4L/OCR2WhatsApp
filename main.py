from get_number import extract_number
from selenium_whatsapp import send_whatsapp_message

numbers_list = []
numbers_list_converted = []
excluded_numbers = []

message = "Olá, tudo bem? Me chamo Marina, estou fazendo uma pesquisa sobre ... você poderia acessar o link e responder? Não levará mais do que 5 minutos. Obrigada!"

extract_number(numbers_list, numbers_list_converted, excluded_numbers)
send_whatsapp_message(numbers_list_converted, message)