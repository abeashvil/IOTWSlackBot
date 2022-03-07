class Message:
    def __init__(self, message):
        self.__query = message['messages'][0]['client_msg_id']
        self.__text = message['messages'][0]['text']

    def getQuery(self):
        return self.__query
    
    def getText(self):
        return self.__text 


