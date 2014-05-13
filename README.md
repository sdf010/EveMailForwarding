EveMailForwarding
=================

A small python script that automatically forwards eve mails to your real email account.

To set this up:

1. Get the script along with the sampleconfig.cfg (you should rename this to "config.cfg")

2. Edit the config and fill in your information
	
	I currently don't have access to an smtp so I made a new googlemail account to use. If you happen to have access to one, just edit the script (line 62) accordingly. Fill in the config file with your information, including a limited api key (Only needs MailMessage and MailBodies, predefined link: https://community.eveonline.com/support/api-key/CreatePredefined?accessMask=2560 ), as well as your characters' ID (Obtain this by running an ID request for your name, spaces in your name equal %20 in the request. An Example: If the characters name is "Martin Sonderberg", the request would be https://api.eveonline.com/eve/CharacterID.xml.aspx?names=Martin%20Sonderberg).
	
3. Profit

	Simply run the script in order to get email updates when evemails get sent to your character, set it up on a server with scheduled runtime (run it every 30 minutes) in order to get regular updates.
	
Word of Caution: Textfiles are not the safest form of storing unencrypted passwords so use this method at your own risk, I will change credential storage in the future, for now feel free to edit the script in whichever way you like.