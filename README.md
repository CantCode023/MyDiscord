<img src="https://cdn.discordapp.com/attachments/918732557103824896/923977976616452146/unknown.png"><br>
Control your Discord client with Python.


# Docs

# Installing required files
1. Make a new file named ".env"
2. Inside .env, write token="YourDiscordTokenHere"
3. Install MyDiscord with pip install mydiscord and install dotenv with pip install python-dotenv
4. Make a new Python file

# NOTE* ALWAYS DO  "pip install -U mydiscord" EVERYDAY TO CHECK IF THERE'S A NEW UPDATE!

# Setting Up The Python File
1. Import required libraries

```python
from mydiscord import Client
from dotenv import load_dotenv
import os
```

2. Load .env and set up your client

``` python
load_dotenv("path_to_your_.env_file")
client = Client(os.environ["token"]])
# Congratulations! Your setup is done!
```

# Setting Status
You can now set your status from old to new!<br>
Arguments needed are: StatusMessage (string)<br>
Version needed: 1.0.7

Example:
```python
statusmesage = "This status is automated with MyDiscord!"

i = client.setStatus(statusmessage)
print(i)

# Check if you've successfully changed your ststus to your new status. If you get an error, please contact us: cantcode023@gmail.com
```

# Making an invite for a Discord server
Arguments needed are: ServerID (int), ChannelID (int), Max_Age (int), Max_Uses (int) and Temporary (boolean).<br>
<strong>NOTE: THESE ARE THE ALLOWED MAX_AGE TYPES, MAX_USES TYPE AND TEMPORARY TYPE
MAX_AGE: [0, 1800, 3600, 21600, 43200, 86400, 604800] 0 means never expires code
MAX_USES: [0, 1, 5, 10, 25, 50, 100] 0 means unlimited
TEMPORARY: True or False</strong><br>
Version needed: 1.0.7

Example:
```python
serverid = 000000000
channelid = 000000000
max_age = 0
max_uses = 0
temporary = False

j = client.makeInvite(serverid, channelid, max_age, max_uses, temporary)
print(j)

# Check if you've successfully made an invite link of the discord server. If you get an error, please contact us: cantcode023@gmail.com
```

# Sending Message
You can send message to a specific channel.<br>
Arguments needed are: ChannelID (int) and Message (int).<br>
Version needed: 1.0.7

Example:
```python
# Right click a channel and click "Copy ID" works with DM, Group DM and Channels in Discord Servers.
channel_id = CHANNELID (integer) # 00000000
message = MESSAGE (string) # "Hello World!"

a,b = client.sendMessage(channel_id, message)
print(a,b) # a is the channel ID and b is the message ID

# Check if you've successfully sent the messsage to a specific channel. If you get an error, please contact us: cantcode023@gmail.com
```

# Deleting Message
You can also delete message.<br>
Arguments needed are: ChannelID (int) and MessageID (int).<br>
Version needed: 1.0.7

Example:
```python
# From the tutorial above "Sending Message", notice that client.sendMessage returns channel Id and message ID, so you can use it to delete message.
c = client.deleteMessage(a,b)
print(c)

# Check if you've successfully deleted the messsage. If you get an error, please contact us: cantcode023@gmail.com
```

# Editing Message
Arguments needed are: ChannelID (int), MessageID (int) and Message (string).<br>
Version needed: 1.0.7

Example:
```python
# Similar to above, you can edit a message with channel id and message id. We'll also use the a and b variable which is a = channel ID and b = message ID.

# You'll also need a new message to edit the old message. You can do it like this
newmessage = "This message is edited!"

d = client.editMessage(a, b, newmessage)
print(d)

# Check if you've successfully edited the messsage. If you get an error, please contact us: cantcode023@gmail.com
```

# Pinning Message
Arguments needed are: ChannelID (int) and MessageID (int).<br>
Version needed: 1.0.7

Example:
```python
# We're also going to be using the a and in b variable in this case.
e = client.pinMessage(a, b)
print(e)

# Check if you've successfully pinned the messsage. If you get an error, please contact us: cantcode023@gmail.com
```

# Reply Message
Arguments needed are: ChannelID (int), MessageID (int) and Message (string).<br>
Version needed: 1.0.7

Example:
```python
# You can also reply to a message. In this case we will be using a and b variables again

# Replying a message needs a message, so let's make one.
replymessage = "This message is replied!"

f = client.replyMessage(a,b,replymessage)
print(f)

# Check if you've successfully replied the messsage. If you get an error, please contact us: cantcode023@gmail.com
```

# Setting Presence
Setting your presence basically means setting your online to invisible or idel or dnd.<br>
Arguments needed are: PresenceType (string)<br>
<strong>NOTE: YOU CAN ONLY USE THESE 4 TYPES OF PRESENCE: online, idle, dnd, invisible. (Capital Sensitive)</strong><br>
Version needed: 1.0.7

Example:
```py
g = client.setPresence("online")
print(g)

# Check if you've successfully changed your presence to a specific presence. If you get an error, please contact us: cantcode023@gmail.com
```


# Adding a new friend
You can also add new friend with MyDiscord<br>
Arguments needed are: User (string) and UserID (int and optional, only use UserID if you get an error.)<br>
Version needed: 1.0.7

Example:
```python
user = "bob#0083"
h = client.addFriend(user)
print(h)

# In case you get an erorr, use UserID
userid = bob's user id (int) #00000000000
h = client.addFriend(user, userid)
print(h)

# Check if you've successfully added user to your pending friend list. If you get an error, please contact us: cantcode023@gmail.com
```

# Remove a friend
You can also remove friend from your friend list.<br>
Argument needed is: UserID (int)<br>
Version needed: 1.0.7

Example:
```python
userid = 00000000000

k = client.removeFriend(userid)
```

# Set note to user
Arguments needed are: UserID (int) NoteMessage (string)<br>
Version needed: 1.0.7

Example:
```python
userid = 00000000000
notename = "This is a note testing!"
l = client.setNo(userid, ntoename)
print(l)

# Check if you've successfully set note to the user. If you get an error, please contact us: cantcode023@gmail.com
```

# Get Friends
Version needed: 1.1.0

Example:
```python
for i in client.getFriends():
    print(i['user']["username"])
```

# Create DM
Argument: UserID (int)<br>
Version needed: 1.1.0

Example:
```python
#  To create dm, you need a user id.
bobid = 00000000000
channel = client.createDM(bobid)

# After creating the channel, you can send message to the dm.

client.sendMessage(channel, "Created DM")
```

# Spread message
Arguments: Message (str), Cooldown, (int)<br>
Version needed: 1.1.0

Example:
```python
spread = client.spreadMessage("Message", 2) # 2 is cooldown
```

# BY THE WAY! ALWAYS REMEMBER TO DO "pip install -U mydiscord" EVERYDAY TO GET THE LASTEST MYDISCORD VERSION!

# THE END OF DOCS! THANKS FOR READING!!
