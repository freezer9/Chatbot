
import re



# This class parses a string to understand the basic queries.
# Author : freezer9




class StringParser(object):

	'''

	StringParser class parses the string to understand what the user is saying or asking.
	Basically It's not doing anything like generating responses or showing responses to the user.

	What is does it that, it figures out what the user wants. Whether the user wants to chat or know.

	'''


	def __init__(self,string):

		self.string = string
		self.string = self.ConvertToLower()
		self.CheckConversation()
		self.RespondToConvo()

	def isStringEmpty(self):

		''' Checks if a string is empty.'''
		return len(self.string) == 0


	def ConvertToLower(self):
		return self.string.lower()


	def CheckConversation(self):
		'''
		This method checks if the user wants to start a conversation.

		Generally convos begin with a greeting. It can be Hey,hi
		This function uses regex to figure out the greetings, since there can
		be other things in a sentence.

		This function isn't gonna respond to the user, because it only notifies the
		other class that the user wants to start a convo.


		'''
		self.Conversation_start = False
		self.ConvoRegx = r'hi|hey|sup|yo'
		self.matched_words = re.findall(self.ConvoRegx,self.string)
		if self.matched_words:
			self.Conversation_start = True
		return self.Conversation_start

	def RespondToConvo(self):
		if self.CheckConversation():
			print('Hello :D')


Chatbot = StringParser("Hey How are you?")
