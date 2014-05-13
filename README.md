EveMailForwarding
=================

A small python script that automatically forwards eve mails to your real email account.

To set this up:

1. Get the script along with the sampleconfig.cfg (you should rename this to "config.cfg")

2. Edit the config and fill in your information
	
	I currently don't have access to an smtp so I made a new googlemail account to use. If you happen
	to have access to one, just edit the script (line 62) accordingly. Fill in the config file with your
	information, including a limited api key (Only needs MailMessage and MailBodies, predefined link: 
	https://community.eveonline.com/support/api-key/CreatePredefined?accessMask=2560 ), as well as your
	characters ID (get this by running an ID request for your name, spaces in your name equal %20 in the request
	example: If the characters name is "Martin Sonderberg", the request would be 
	https://api.eveonline.com/eve/CharacterID.xml.aspx?names=Martin%20Sonderberg).
	
3. Profit

	Simply run the script in order to get emailes about changes, set it up on a virtual server
	
Word of Caution: Textfiles are not the safest form of storing unencrypted passwords so use this method
at your own risk.