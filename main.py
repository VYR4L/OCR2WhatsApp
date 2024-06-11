from get_number import extract_number
from selenium_whatsapp import send_whatsapp_message

numbers_list = []
numbers_list_converted = []
excluded_numbers = []

message = "<your message>"
link = "<your_link"
extract_number(numbers_list, numbers_list_converted, excluded_numbers)
send_whatsapp_message(numbers_list_converted, message, link)
