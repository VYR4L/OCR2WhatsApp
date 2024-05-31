from get_number import extract_number
from selenium_whatsapp import send_whatsapp_message

numbers_list = []
numbers_list_converted = []
excluded_numbers = []

message = "Olá, prof! Tudo bem?!\nNão é telemarketing ou spam 😅\nMe chamo Marina, sou doutoranda em Educação na Universidade Estadual do Oeste do Paraná (Unioeste).\nRealizo uma pesquisa com professores da rede estadual de ensino de Mato Grosso. Tem sido bem difícil encontrar os professores, por isso tenho buscado, pessoalmente, entrar em contato. Posso contar com sua ajuda para responder o formulário da pesquisa? Dura 5min, no máximo!\nÉ sigiloso e anônimo!\nSe puder repassar aos contatos conhecidos, agradeço muito! 🙏🏻"
link = "https://docs.google.com/forms/d/e/1FAIpQLSeCsytjpURRLgiEClRggardOoCiCeWbP-MBwyq5ELwMJKgWQA/viewform"
extract_number(numbers_list, numbers_list_converted, excluded_numbers) #Aqui a o codigo extrai os numero
send_whatsapp_message(numbers_list_converted, message, link) # Aqui o codigo ira mandar as msgs
