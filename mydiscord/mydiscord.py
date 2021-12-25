import requests
import json
import traceback

class Discriminator:
    def toDis(number):
        a = []

        for i in range(len(number)):    
            a.append(i)

        for i in a:
            if number[i] == "0":
                if i == len(number)-1:
                    if number[i-1] == "0":
                        number = number
                    elif number[0] != "0":
                        number = number
                    else:
                        number = number[:i]
                elif i == 0:
                    if number[-1] == "0":
                        pass
                    else:
                        number = number[i+1:]
                
        return number

class Client:
    def __init__(self, token:str):
        self.token = token

    def setStatus(self, status:str):
        url = "https://discord.com/api/v9/users/@me/settings"
        headers = {
            "authorization": self.token,
            "content-type": "application/json"
        }
        data = str({"custom_status": {"text": str(status)}}).replace("'",'"')
        try:
            resp = requests.patch(url, headers=headers, data=data)
            if resp.status_code == 200:
                return json.loads(resp.text)
            else:
                return "There was an error! Please check your arguments again."
        except Exception:
            return "There was an error!{}".format(traceback.format_exc())

    def makeInvite(self, serverid:int, channelid:int, max_age:int=604800, max_uses:int=0, temporary:bool=False):
        ages = [0, 1800, 3600, 21600, 43200, 86400, 604800]
        uses = [0, 1, 5, 10, 25, 50, 100]
        url = f"https://discord.com/api/v9/channels/{str(channelid)}/invites"
        headers = {"authorization": self.token}
        
        data = {
            "max_age": max_age,
            "max_uses": max_uses,
            "temporary": temporary
        }

        ij = f"https://discord.com/channels/{str(serverid)}/{str(channelid)}"
        b = requests.get(ij, headers=headers, data=data).text
        b = str(b)
        if 'id="app-mount"' in b:
            if max_age in ages:
                if max_uses in uses:
                    try:
                        resp = requests.post(url, headers=headers, data=data)
                        resp1 = json.loads(resp.text)
                        if resp.status_code == 200:
                            return f"https://discord.com/invite/{resp1['code']}"
                        else:
                            return "There was an error! Please check your aruguments again. "
                    except Exception:
                        return "There was an error!\n{}".format(traceback.format_exc())
                else:
                    return "Wrong max_uses format! Please read the documentation."
            else:
                return "Wrong max_age format! Please read the documentation."
        else:
            return "Unvalid server!"

    def sendMessage(self, channel_id:int, message:str):
        url = f"https://discord.com/api/v6/channels/{channel_id}/messages"
        headers = {
            "authorization": self.token
        }

        data = {
            "content": message
        }

        try:
            resp = requests.post(url, headers=headers, data=data)
            resp1 = json.loads(resp.text)
            if resp.status_code == 200:
                return resp1['channel_id'], resp1['id']
            else:
                return "There was an error! Pleace check your arguments."
        except Exception:
            return "There was an error!\n{}".format(traceback.format_exc())

    def deleteMessage(self, channel_id:int, message_id:int):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
        headers = {
            "authorization": self.token
        }
        try:
            resp = requests.delete(url, headers=headers)
        except Exception:
            return "There was an error!\n{}".format(traceback.format_exc())

    def pinMessage(self, channel_id:int, message_id:int):
        url = f"https://discord.com/api/v9/channels/{channel_id}/pins/{message_id}" 
        headers = {
            "authorization": self.token
        }
        try:
            resp = requests.put(url, headers=headers)
        except Exception:
            return "There was an error!\n{}".format(traceback.format_exc())

    def editMessage(self, channel_id:int, message_id:int, message:str):
        url = f"https://discord.com/api/v6/channels/{channel_id}/messages/{message_id}"
        headers = {
            "authorization": self.token
        }
        data = {
            "content": message
        }
        try:
            resp = requests.patch(url, headers=headers, data=data)
            resp1 = json.loads(resp.text)
            if resp.status_code == 200:
                return "Successfull edited message"
            else:
                return "There was an error! Please check your arguments."
        except Exception:
            return "There was an error!\n{}".format(traceback.format_exc())

    def replyMessage(self, channel_id:int, message_id:int, message:str):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        
        headers = {"authorization": self.token}
        
        data = {
            "content": message,
            "message_reference": {
                "channel_id": channel_id,
                "message_id": message_id
            }
        }

        try:
            resp = requests.post(url, headers=headers, data=data)
            resp1 = json.loads(resp.text)
            if resp.status_code == 200:
                return resp1
            else:
                return "There was an error! Please check your arguments."
        except Exception:
            return  "There was an error!\n{}".format(traceback.format_exc())

    def setPresence(self, presence:str=["online", "idle", "dnd", "invisible"]):
        allowedPresence = ["online", "idle", "dnd", "invisible"]
        url = "https://discord.com/api/v9/users/@me/settings"

        headers = {
            "authorization": self.token
        }
        if presence in allowedPresence:
            data = {
                "status": presence.lower()
            }
            try:
                resp = requests.patch(url, headers=headers, data=data)
                resp1 = json.loads(resp.text)
                if resp.status_code == 200:
                    return resp1
                else:
                    return "There was an erorr! Please check your arguments."
            except Exception:
                return "There was an erorr!\n{}".format(traceback.format_exc())

    def addFriend(self, user:str="test#0000", id:int=None):
        url = "https://discord.com/api/v9/users/@me/relationships"
        
        headers = {
            "authorization": self.token
        }

        a = user.split("#")[0]
        b = Discriminator.toDis(user.split("#")[1])
        data = {
            "username": a,
            "discriminator": b
        }
        try:
            resp = requests.post(url, headers=headers, data=data)
            if resp.status_code == 204:
                return "Added " + user
            else:
                return "There was an erorr! Please check your arguments."
        except:
            url = "https://discord.com/api/v9/users/@me/relationships/" + str(id)
            
            headers = {
                "authorization": self.token
            }

            data = {}

            try:
                resp = requests.put(url, headers=headers, data=data)
                if resp.status_code == 204:
                    return "Added " + user
                else:
                    return "There was an erorr! Please check your arguments."
            except Exception:
                return "There was an error!\n{}".format(traceback.format_exc())