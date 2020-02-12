from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

#from rasa_core_sdk import Action
#from rasa_core_sdk.events import SlotSet
#from rasa_core.actions.action import Action
#from rasa_core.events import SlotSet
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import json
import requests

class ActionLoanOffer(Action):
	def name(self):
		return 'action_loanoffer'

	def run(self, dispatcher, tracker, domain):
		'''
		amount = tracker.get_slot('l_amt')
		m_pay = tracker.get_slot('monthly_pay')
		comp = tracker.get_slot('company')
		cus_name = tracker.get_slot('name')
		DOB = tracker.get_slot('dob')
		dtype = tracker.get_slot('doc_type')
		'''

		ltype = tracker.get_slot('loantype')

		#print("\n",ltype,"\n")
		dispatcher.utter_message("\n LOAN OFFER FOR YOU : \n")
		response = ""
		if ltype == "house":
			response = "\nDEFAULT OFFER  ::::::::::::::\n     You could buy a house, you will need to pay Rs. 5 Lakhs as down payment and loan will be for 15 years. Which means you will repay back in 180 monthly installments of Rs. 8333 only. You could get the loan on 0 percent interest rate for the first 6 months of repayment\n"	

		elif ltype == "car":
			response = "\nDEFAULT OFFER  :::::::::::::\n     This is a default offer programmed by my creator(https://github.com/divi97). For a real offer I need a database to process that. Sorry for any inconvenience caused. Have a Great Day!!\n\n"
		
		elif ltype == "electronics":
			response = "\nDEFAULT OFFER   :::::::::::::\n     This is a default offer programmed by my creator(https://github.com/divi97). For a real offer I need a database to process that. Sorry for any inconvenience caused. Have a Great Day!!\n\n"

		elif ltype == "business":
			response = "\nDEFAULT OFFER  ::::::::::::::\n    This is a default offer programmed by my creator(https://github.com/divi97). For a real offer I need a database to process that. Sorry for any inconvenience caused. Have a Great Day!!\n\n"

		elif ltype == "festival":
			response = "\nDEFAULT OFFER  ::::::::::::::\n    This is a default offer programmed by my creator(https://github.com/divi97). For a real offer I need a database to process that. Sorry for any inconvenience caused. Have a Great Day!!\n\n"

		elif ltype == "marriage":
			response = "\nDEFAULT OFFER  ::::::::::::::\n    This is a default offer programmed by my creator(https://github.com/divi97). For a real offer I need a database to process that. Sorry for any inconvenience caused. Have a Great Day!!\n\n"

	
		dispatcher.utter_message(response)
		return [SlotSet('loantype', ltype)]

class ActionValidateCompany(Action):
	def name(self):
		return 'action_validate_company'
	
	def run(self, dispatcher, tracker, domain):
		comp = tracker.get_slot('company')
		valid_company = ['intel','ibm','maruti','suzuki','audi','bmw','bugatti','oracle','honda','mitsubishi','hyundai','ferrari','toyota','tata','lamborghini','nissan','reliance','vadaphone','airtel','nucleus software exports limited','nucleus software exports','nucleus software exports ltd.','nucleus software exports ltd','nucleus','nucleus software','infosys','wipro', 'tata consulatancy services','tcs','samsung','sony','panasonic','lenovo','hp','tupperware','lg','google','apple','xiaomi','nokia','adidas','reebok','puma','sketchers','nike','wrangler','microsoft','amazon','facebook','alibaba','walmart','flipkart']
		if comp.lower() not in valid_company:
			dispatcher.utter_message(" Sorry, I haven't heard of it.")
			return [SlotSet('company', comp)]
		else:
			dispatcher.utter_message(" It's a great company to work for. It will get you a favourable view.")
			return [SlotSet('company', comp)]

'''
class ActionCibilScore(Action):
	def name(self):
		return 'action_cibil_score'

	def run(self, dispatcher, tracker, domain):
		return [SlotSet('')]
'''


# In similar way like Actions, Slots can also be pre-processed or at run-time at the action server end

# \nThis is a default offer programmed by my creator(https://github.com/divi97). For a real offer I need a database to process that. Sorry for any inconvenience caused. Have a Great Day!!\n
