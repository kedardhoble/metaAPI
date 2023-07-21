import requests

page_id = '855743759471787'
page_access_token='EAAKP1WDlOnQBAKmd1GNtTuyAoBPTbx4v6HZArLmynyZCHMhZC0SZBZAAGrFTTzYID5sCZAq2sPSX5TJVzSCZCWbJmzmtMMcIFaq9FsYaiA0byoi8J1vwKZCaDb69OwcVzKCBgfO6bfEgUOcDa8ZB8xSCiWfGAtRNK07T6PZA2fxoQuoyAEdxzmHbBN6ZBRwdhHEF88AuWfopltY8b8cmM1qEqjj'
user_access_token = 'EAAKP1WDlOnQBAPwvPPUg0jXTcPtwqHOvwA6h2h18NPivvTPPmc80iAQvubrE5dLqTZAGRPbgj0u9DlffRabWQPh5tVOZBeA51DywA6p4BIZCGMblojFDxNbZAqrIeFXf7xx2O31nacZAyGMLJZB84j8XmJwmTQacOBO057nlpJU5zBYGRROL9Ddnz3zMpia1uMszOJU8C3GFq8JPjsukTZBxJRaZAmcwFlcZD'

### get PSID
# def get_psid(page_id, page_access_token):
#     url = f'https://graph.facebook.com/{page_id}/conversations?fields=participants&access_token={page_access_token}'
#     response = requests.get(url)
#     data = response.json()
#     if "data" in data and data["data"]:
#         participants_data = data["data"][0].get("participants", {}).get("data", [])
#         psid_list = [participant.get("id") for participant in participants_data if participant.get("id")]
#         return psid_list
#     return None
# psid_list = get_psid(page_id, page_access_token)
# if psid_list:
#     print("PSIDs found:")
#     for psid in psid_list:
#         print(psid)
# else:
#     print("No PSIDs found.")

# def get_psid():
# response = requests.get(f'https://graph.facebook.com/{page_id}/conversations?fields=participants&access_token={page_access_token}')
# print(response.json())
    # return get_psid
    
### get conversations

def get_facebook_messages(conversation_id, page_access_token):
    get_messages_uri = f"https://graph.facebook.com/{conversation_id}?fields=messages{message}&access_token={page_access_token}"
    response = requests.get(get_messages_uri)
    return response.json()
if __name__ == "__main__":    
    conversation_id = 't_3563069910589053'
    message = "{message}"
    messages_response = get_facebook_messages(conversation_id, page_access_token)
    print(messages_response)    
get_messagees_uri = f"https://graph.facebook.com/{conversation_id}?fields=messages{message}&access_token={page_access_token}"
response = requests.get(get_messagees_uri)
print(response.json())

### send message to customer

# recipient_id = "{id:107674589063136}"
# text = "{text:'You did it!'}"
# send_message_uri = """https://graph.facebook.com/v14.0/{page_id}/messages?recipient={recipient_id}&message={text}&messaging_type=RESPONSE&access_token={page_access_token}""".format(page_id=page_id, recipient_id=recipient_id, text=text, page_access_token=page_access_token)
# response = requests.post(send_message_uri)
# print(response.json())
