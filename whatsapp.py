import pywhatkit

# Variables
phone_numer = ''
group_id = ''
message = 'Write the message here'
time_hour = 16
time_minute = 00
waiting_time_to_send = 10
close_tab = True
waiting_time_to_close = 20

mode = "contact"

if mode == "contact":
    # Send a WhastApp message to an specific contact
    pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
elif mode == "group":
    # Send a WhastApp message to an specific group
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")
