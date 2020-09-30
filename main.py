# Robert Hollinger
# Last edited 9/29/2020
import fbchat
import time

username = input("What is your facebook username?: ")
passW = input("What is your password?: ")
client = fbchat.Client(username, passW)
search = input("Who do you want to send message to?: ")
users = client.searchForUsers(search)
user = users[0]
msg = str(input("What do you want to send?: "))
client.send(fbchat.models.Message(msg), user.uid)
time.sleep(120)  # Wait 2 minutes before logging back out (prevent getting blocked)
client.logout()  # Securely log out after use


